from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import MetaData, Table, Column, String, Integer, DateTime, Boolean
from sqlalchemy.orm import relationship
from datetime import datetime

Base = declarative_base()

class HealthcareWorker(Base):
    __tablename__ = 'healthcareworker'
    name = Column('', String(50))
    created = Column('created_on', DateTime, default=datetime.utcnow)
    id = Column('', Integer, primary_key=True)

    def retData(self):
        return {'name': self.name}

class Paciente(Base):
    __tablename__ = 'paciente'
    name = Column('', String(50))
    created = Column('created_on', DateTime, default=datetime.utcnow)
    id = Column('', Integer, primary_key=True)

    def retData(self):
        return {'name': self.name}
