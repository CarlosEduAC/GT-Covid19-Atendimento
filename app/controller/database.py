from sqlalchemy.orm import Session
from sqlalchemy import create_engine 
import pandas as pd
import datetime

DATABASE_URL = 'mysql+pymysql://covid:Covid_UFF_UFRJ@10.77.0.29:3306/atendimento_covid_teste'

class Database():
    engine = create_engine(DATABASE_URL, echo=False)
    s = Session(bind=engine)

    def __init__(self):
        self.connection = self.engine.connect()
        print("DB Instance created")
    
    def saveData(self, data):
        session = Session(bind=self.connection)  
        session.add(data)
        session.commit()
    
    def saveIfNew(self, obj):
        session = Session(bind=self.engine)
        res = session.query(type(obj)).filter_by(**obj.retData()).first()
        if res:
            return res.id
            
        session.add(obj)
        session.flush()
        session.commit()
        return session.query(type(obj)).filter_by(**obj.retData()).first().id

    def select(self, obj):
        session = Session(bind=self.engine)
        if list(set(obj.retData().values()))[0] == None:
            return pd.read_sql(session.query(type(obj)).statement, session.bind)
        else:
            return pd.read_sql(session.query(type(obj)).filter_by(**obj.retData()).statement, session.bind)