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

    def select(self, data):
        newData = []
        session = Session(bind=self.engine)
        result = session.query(data).all()

        for r in result:
            newData.append((r.idComorbidades, r.Descricao))

        return newData