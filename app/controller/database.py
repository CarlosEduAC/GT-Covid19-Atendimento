from api.models import *
from sqlalchemy.orm import Session
import sqlalchemy as db 
import pandas as pd
import datetime

DATABASE_URL = 'mysql+pymysql://admin:gtCovid19*2020@covid-19.csrnyzd4qxmh.sa-east-1.rds.amazonaws.com/covid-19'

class Database():
    engine = db.create_engine(DATABASE_URL, pool_size=200, echo=False, pool_pre_ping=True)
    s = Session(bind=engine)

    def __init__(self):
        self.connection = self.engine.connect()
        print("DB Instance created")
    
    def saveData(self, data):
        session = Session(bind=self.connection)        
        session.add(data)
        session.commit()