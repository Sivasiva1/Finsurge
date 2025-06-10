import os
import sys
import time
import json
import logging
from pathlib import Path
from urllib.parse import quote_plus

import sqlalchemy
import pandas as pd

from conf.loadConfig import conf as config

# Read and setup DB engine
engine = sqlalchemy.create_engine(
    f"mysql+pymysql://{config.mysqlUser}:{quote_plus(config.mysqlPassword)}@{config.mysqlHost}:{config.mysqlPort}/{config.mysqlDb}?charset=utf8&local_infile=1",
    pool_recycle=600,
    max_overflow=20,
    pool_size=config.pool_size
)

logger = logging.getLogger(f"tv.{Path(__file__).stem}")
os.makedirs("tv-etl/logs", exist_ok=True)
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler("tv-etl/logs/housekeeping.log"),
        logging.StreamHandler(sys.stdout)
    ]
)

def construct_where_clause(table_conf):
    table_name = table_conf["table_name"]
    logger.info("Processing table: %s", table_name)

    retention_value = table_conf["retention_period"]["value"]
    retention_unit = table_conf["retention_period"]["unit"]
    custom_where = table_conf.get("custom_where", "")
    date_columns = table_conf.get("date_columns", [])

    interval = f"INTERVAL {retention_value} {retention_unit.upper()}"
    date_conditions = [f"{col} < NOW() - {interval}" for col in date_columns]

    where_clauses = []
    if custom_where:
        where_clauses.append(custom_where)
    if date_conditions:
        where_clauses.append(" AND ".join(date_conditions))

    if not where_clauses:
        return None

    return " AND ".join(where_clauses)

def construct_select_query(table_conf):
    table_name = table_conf["table_name"]
    where_clause = construct_where_clause(table_conf)
    if not where_clause:
        return None
    return f"SELECT COUNT(*) FROM {table_name} WHERE {where_clause}"

class DatabaseHousekeeping:
    def __init__(self, config_file):
        self.config_file = config_file
        self.logger = logger

    def sqlExecuteQuery(self, query):
        try:
            with engine.begin() as conn:
                conn.execute(sqlalchemy.text(query))
        except sqlalchemy.exc.OperationalError as operr:
            self.logger.warning("OperationalError: %s", operr)
            if "lost connection" in str(operr).lower() or "lock table" in str(operr).lower():
                time.sleep(config.get("retry_delay", 10))
                return self.sqlExecuteQuery(query)
            raise
        except Exception:
            self.logger.exception("Failed executing query")
            raise

    def run(self):
        self.logger.info("Starting housekeeping process")
        try:
            with open(self.config_file, "r") as f:
                config_json = json.load(f)

            tables = config_json.get("tables", [])

            for table_conf in tables:
                select_query = construct_select_query(table_conf)
                if not select_query:
                    self.logger.warning(f"No valid WHERE clause for table: {table_conf['table_name']}. Skipping.")
                    continue

                self.logger.info("Select Query: %s", select_query)
                # You can execute or log the result here using self.sqlExecuteQuery(select_query)

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
        housekeeping = DatabaseHousekeeping(config_file)
        housekeeping.run()
        sys.exit(0)
    except Exception as e:
        logger.exception("Fatal error in main")
        sys.exit(1)
