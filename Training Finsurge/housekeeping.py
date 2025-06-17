import os
import sys
import time
import json
import logging
from pathlib import Path
from urllib.parse import quote_plus

import sqlalchemy
from conf.loadConfig import conf as config

# DB Engine
engine = sqlalchemy.create_engine(
    f"mysql+pymysql://{config.mysqlUser}:{quote_plus(config.mysqlPassword)}@{config.mysqlHost}:{config.mysqlPort}/{config.mysqlDb}?charset=utf8&local_infile=1",
    pool_recycle=600,
    max_overflow=20,
    pool_size=config.pool_size
    
)
def setup_logger(config):
    log_level = getattr(logging, config.get("log_level", "INFO").upper(), logging.INFO)
    log_dir = config.get("log_dir", "logs")
    os.makedirs(log_dir, exist_ok=True)

    logger = logging.getLogger(f"tv.{Path(__file__).stem}")
    logger.setLevel(log_level)

    if not logger.hasHandlers():
        formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")

        file_handler = logging.FileHandler(os.path.join(log_dir, "housekeeping.log"))
        file_handler.setFormatter(formatter)
        file_handler.setLevel(log_level)

        stream_handler = logging.StreamHandler(sys.stdout)
        stream_handler.setFormatter(formatter)
        stream_handler.setLevel(log_level)

        logger.addHandler(file_handler)
        logger.addHandler(stream_handler)

    return logger

def construct_where_clause(table_conf):
    retention_value = table_conf["retention_period"]["value"]
    retention_unit_raw = table_conf["retention_period"]["unit"].strip().lower()
    custom_where = table_conf.get("custom_where", "")
    date_columns = table_conf.get("date_columns", [])

    # Map plural or invalid forms to valid MySQL interval units
    unit_mapping = {
        "days": "DAY",
        "day": "DAY",
        "months": "MONTH",
        "month": "MONTH",
        "years": "YEAR",
        "year": "YEAR"
    }

    if retention_unit_raw not in unit_mapping:
        raise ValueError(f"Unsupported retention unit: {retention_unit_raw}")

    retention_unit = unit_mapping[retention_unit_raw]
    interval = f"INTERVAL {retention_value} {retention_unit}"

    date_conditions = [f"{col} < NOW() - {interval}" for col in date_columns]

    where_clauses = []
    if custom_where:
        where_clauses.append(custom_where)
    if date_conditions:
        where_clauses.append(" AND ".join(date_conditions))

    if not where_clauses:
        return None
    return " AND ".join(where_clauses)

def construct_parent_delete_query(table_conf, batch_size):
    table_name = table_conf["table_name"]
    where_clause = construct_where_clause(table_conf)
    if not where_clause:
        return None
    return f"""
        DELETE FROM {table_name}
        WHERE ID IN 
            (
                SELECT ID FROM {table_name}
                WHERE {where_clause}
                LIMIT {batch_size}
            ) 
        
    """
def construct_dual_parent_child_delete_query(table_conf, batch_size):
    """
    Construct delete query for a junction table that depends on two parent tables.
    """
    table_name = table_conf["table_name"]
    where_clause = construct_where_clause(table_conf)
    if not where_clause:
        return None

    dual_fk_conditions = []
    for fk in table_conf.get("foreign_key", []):
        if fk.get("parent_table") is False:
            parent_table = fk["table_name"]
            parent_col = fk["parent_column"]
            child_col = fk["child_column"]
            condition = f"{child_col} IN (SELECT {parent_col} FROM {parent_table} WHERE {where_clause})"
            dual_fk_conditions.append(condition)

    if not dual_fk_conditions:
        return None

    # Combine both FK conditions with AND for stricter deletion
    combined_condition = " AND ".join(dual_fk_conditions)

    return f"""DELETE FROM {table_name} 
                WHERE {combined_condition} 
                LIMIT {batch_size}"""

def construct_child_delete_queries(table_conf, batch_size):
    """
    Generate delete queries for child tables based on parent table's retention WHERE clause.
    """
    parent_table = table_conf["table_name"]
    where_clause = construct_where_clause(table_conf)
    if not where_clause:
        return []

    queries = []
    for fk in table_conf.get("foreign_key", []):
        if fk.get("parent_table"):
            child_table = fk["table_name"]
            parent_col = fk["parent_column"]
            child_col = fk["child_column"]

            query = f"""
                DELETE FROM {child_table}
                WHERE {child_col} IN (
                        SELECT {parent_col} FROM {parent_table}
                        WHERE {where_clause}
                        LIMIT {batch_size}
                    ) 
                
            """
            
            queries.append((child_table, query))
    return queries

def construct_select_query(table_conf):
    table_name = table_conf["table_name"]
    where_clause = construct_where_clause(table_conf)
    if not where_clause:
        return None
    return f"SELECT COUNT(*) as count FROM {table_name} WHERE {where_clause}"
def construct_dual_parent_select_query(table_conf):
    """
    Construct select count query when table has two parent tables (junction table case).
    """
    table_name = table_conf["table_name"]
    where_clause = construct_where_clause(table_conf)
    if not where_clause:
        return None

    dual_fk_conditions = []
    for fk in table_conf.get("foreign_key", []):
        if fk.get("parent_table") is False:  # explicitly false
            parent_table = fk["table_name"]
            parent_col = fk["parent_column"]
            child_col = fk["child_column"]
            condition = f"{child_col} IN (SELECT {parent_col} FROM {parent_table} WHERE {where_clause})"
            dual_fk_conditions.append(condition)

    if not dual_fk_conditions:
        return None

    # Combine both conditions with AND
    dual_condition = " AND ".join(dual_fk_conditions)
    return f"SELECT COUNT(*) as count FROM {table_name} WHERE {dual_condition}"

def construct_delete_query(table_conf, batch_size):
    table_name = table_conf["table_name"]
    where_clause = construct_where_clause(table_conf)
    if not where_clause:
        return None
    return f"""DELETE FROM {table_name}
                WHERE {where_clause}
                LIMIT {batch_size}"""

class DatabaseHousekeeping:
    def __init__(self, config):
            self.config = config 
            self.logger = logger
            self.batch_size = config.get("batch_size", 10000)
            self.max_retry = config.get("max_retries",3)
            self.retry_delay = config.get("retry_delay", 10)
            self.transaction_timeout = config.get("transaction_timeout", 300)
            self.verbose_logging = config.get("verbose_logging", False) 
    def fetch_count(self, query):
        try:
            with engine.connect() as conn:
                result = conn.execute(sqlalchemy.text(query)).scalar()
                return result
        except Exception:
            self.logger.exception("Failed to fetch count")
            raise

    def execute_delete_loop(self, table_name, delete_query, total_count):
            total_deleted = 0
            retry_count = 0

            self.logger.info(">>> Starting deletion for table: %s", table_name)
            self.logger.info(">>> Total rows eligible for deletion: %d", total_count)

            while total_deleted < total_count and retry_count < self.max_retry:
                try:
                    with engine.begin() as conn:
                        result = conn.execute(sqlalchemy.text(delete_query))
                        deleted_count = result.rowcount
                        total_deleted += deleted_count

                        self.logger.info("Deleted %d rows in this batch (Total deleted: %d/%d)", 
                                        deleted_count, total_deleted, total_count)

                        if deleted_count == 0:
                            retry_count += 1
                            self.logger.warning("Zero rows deleted. Retry %d/%d", retry_count, self.max_retry)
                            if retry_count >= self.max_retry:
                                self.logger.error("Stopping retries for safety. Reached max retries.")
                                break
                            time.sleep(self.retry_delay)
                        else:
                            retry_count = 0  # Reset if deletion successful

                except Exception:
                    self.logger.exception("Error during deletion for table: %s", table_name)
                    raise

            # Log final status
            try:
                with engine.connect() as conn:
                    post_delete_count = conn.execute(
                        sqlalchemy.text(f"SELECT COUNT(*) FROM {table_name}")
                    ).scalar()
            except Exception:
                self.logger.warning("Failed to fetch post-delete count for table: %s", table_name)
                post_delete_count = "Unknown"

            self.logger.info(">>> Finished deletion for table: %s", table_name)
            self.logger.info(">>> Total rows deleted: %d", total_deleted)
            self.logger.info(">>> Post-deletion row count in table '%s': %s", table_name, post_delete_count)

            if total_deleted < total_count:
                    self.logger.warning("Deleted rows (%d) less than expected (%d). Please verify conditions.", total_deleted, total_count)
            elif total_deleted > total_count:
                    self.logger.warning("Deleted more rows (%d) than counted (%d). Please verify query logic.", total_deleted, total_count)
            else:
                    self.logger.info("Deletion complete for table with %d rows.", total_count)

    def run(self):
        self.logger.info("Starting housekeeping process")
        try:
            tables = self.config.get("tables", [])

            for table_conf in tables:
                table_name = table_conf.get("table_name")
                self.logger.info("Checking table: %s", table_name)

                is_parent = any(fk.get("parent_table") for fk in table_conf.get("foreign_key", []))
                is_dual_parent = (
                    len(table_conf.get("foreign_key", [])) == 2
                    and all(fk.get("parent_table") is False for fk in table_conf["foreign_key"])
                )

                if is_parent:
                    self.logger.info("Processing parent table: %s", table_name)

                    where_clause = construct_where_clause(table_conf)
                    if not where_clause:
                        self.logger.warning("No valid WHERE clause. Skipping table: %s", table_name)
                        continue

                    count_query = construct_select_query(table_conf)
                    self.logger.info("Count Query: %s", count_query)
                    total_count = self.fetch_count(count_query)
                    if total_count == 0:
                        self.logger.info("No records to delete in table: %s", table_name)
                        continue

                    # 1. Delete from child tables first
                    child_queries = construct_child_delete_queries(table_conf, self.batch_size)
                    for child_table, delete_query in child_queries:
                        self.logger.info("Executing delete for child table: %s", child_table)
                        self.execute_delete_loop(delete_query, total_count)
                        self.logger.info("Chile Delete Query for table : %s", delete_query)
                        
                    # 2. Delete from parent table
                    parent_delete_query = construct_parent_delete_query(table_conf, self.batch_size)
                    self.logger.info("Executing delete for parent table: %s", table_name)
                    self.execute_delete_loop(parent_delete_query, total_count)
                    self.logger.info("Parent Delete Query for table : %s", parent_delete_query)
                               
                elif is_dual_parent:
                    self.logger.info("Processing dual-parent junction table: %s", table_name)

                    count_query = construct_dual_parent_select_query(table_conf)
                    delete_query = construct_dual_parent_child_delete_query(table_conf, self.batch_size)

                    self.logger.info("Count Query: %s", count_query)
                    self.logger.info("Delete Query: %s", delete_query)

                    total_count = self.fetch_count(count_query)
                    if total_count == 0:
                        self.logger.info("No records to delete in child table: %s", table_name)
                        continue

                    self.execute_delete_loop(delete_query, total_count)

                    for fk in table_conf["foreign_key"]:
                        parent_table_conf = {
                            "table_name": fk["table_name"],
                            "date_columns": table_conf["date_columns"],
                            "retention_period": table_conf["retention_period"],
                            "custom_where": table_conf.get("custom_where", "")
                        }
                        parent_delete_query = construct_delete_query(parent_table_conf, self.batch_size)
                        self.logger.info("Parent Delete Query (%s): %s", fk["table_name"], parent_delete_query)
                        parent_total_count = self.fetch_count(construct_select_query(parent_table_conf))
                        if parent_total_count == 0:
                            self.logger.info("No deletable rows in parent table: %s", table_name)
                            continue
                        self.execute_delete_loop(parent_delete_query, parent_total_count)

                else:
                    self.logger.info("Processing standalone table (no child): %s", table_name)

                    count_query = construct_select_query(table_conf)
                    self.logger.info("Count Query: %s", count_query)
                    total_count = self.fetch_count(count_query)
                    if total_count == 0:
                        self.logger.info("No records to delete in table: %s", table_name)
                        continue

                    delete_query = construct_delete_query(table_conf, self.batch_size)
                    self.logger.info("Delete Query for table : %s", delete_query)
                    self.logger.info("Executing delete for table: %s", table_name)
                    self.execute_delete_loop(delete_query, total_count)

        except FileNotFoundError:
            self.logger.error(f"Config file not found: {self.config_file}")
            raise
        except json.JSONDecodeError:
            self.logger.error("Invalid JSON in config file")
            raise
        except Exception:
            self.logger.exception("Unexpected error in housekeeping")
            raise

if __name__ == "__main__":
    config_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'conf', 'housekeeping.json')
    
    try:
        with open(config_file, 'r') as f:
             config = json.load(f)

        logger = setup_logger(config)

        # Still pass config_file to your class
        housekeeping = DatabaseHousekeeping(config)
        housekeeping.run()
        sys.exit(0)
    except Exception:
        logger.exception("Fatal error in main")
        sys.exit(1)
