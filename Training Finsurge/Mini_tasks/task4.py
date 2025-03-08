import pandas as pd
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import pymysql 
# Define Base Model
Base = declarative_base()

class Employee(Base):
    __tablename__ = 'emp'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    
    age = Column(Integer)
    city = Column(String, nullable=False)
    salary = Column(Integer)
    department = Column(String)
    joining_date = Column(String)
    performance_score = Column(Integer)

# Database Connection
engine = create_engine("mysql+pymysql://root:Sivakutty123@localhost/dummy")
Session = sessionmaker(bind=engine)
session = Session()

def upsert_from_csv(csv_path):
    
    df = pd.read_csv(csv_path)
    
    for _, row in df.iterrows():
        
            # Check if there is an existing record with the same name and city
            existing_record = session.query(Employee).filter_by(name=row['name'], city=row['city']).first()
            
            if existing_record:
                existing_record.age = row['age']
                existing_record.salary = row['salary']
                existing_record.department = row['department']
                existing_record.joining_date = row['joining_date']
                existing_record.performance_score = row['performance_score']

            else:
                # Check if the `id` exists but with a different name or city
                id_record = session.query(Employee).filter_by(id=row['id']).first()
                
                if id_record and (id_record.name != row['name'] or id_record.city != row['city']):
                    #exists but with a different Name/City -> Inserting as a new row")
                    
                    new_record = Employee(
                        id=None,  
                        name=row['name'], city=row['city'],
                        age=row['age'], salary=row['salary'], department=row['department'],
                        joining_date=row['joining_date'], performance_score=row['performance_score']
                    )
                    session.add(new_record)
                    
                else:
                    new_record = Employee(
                        id=row['id'], name=row['name'], city=row['city'],
                        age=row['age'], salary=row['salary'], department=row['department'],
                        joining_date=row['joining_date'], performance_score=row['performance_score']
                    )
                    session.add(new_record)
                    
    session.commit()
    print("Bulk insert/update completed")
