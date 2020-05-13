from api.models import *
from sqlalchemy.orm import Session
import sqlalchemy as db 
import pandas as pd
import datetime

DATABASE_URL = 'mysql+pymysql://admin:gtCovid19*2020@covid-19.csrnyzd4qxmh.sa-east-1.rds.amazonaws.com:3306/covid-19'

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

    def saveIfNew(self, obj):
        session = Session(bind=self.engine)
        res = session.query(type(obj)).filter_by(**obj.retData()).first()
        if res:
            return res.id
        session.add(obj)
        session.flush()
        session.commit()
        return session.query(type(obj)).filter_by(**obj.retData()).first().id

    def saveIfNewBulk(self, objList):
        session = Session(bind=self.engine)
        res = session.query(type(objList[0])).all()
        def remKeys(rowDict, oList):
            for key in rowDict.keys():
                if key not in oList[0].retData().keys():
                    del rowDict[key]
            return rowDict
        dictList = [remKeys(v.retData(), objList) for v in res]
        for it in objList:
            if it.retData() not in dictList:
                session.add(it)
        session.commit()
        return True

    def select(self, obj):
        session = Session(bind=self.engine)
        if list(set(obj.retData().values()))[0] == None:
            return pd.read_sql(session.query(type(obj)).statement, session.bind)
        else:
            return pd.read_sql(session.query(type(obj)).filter_by(**obj.retData()).statement, session.bind)