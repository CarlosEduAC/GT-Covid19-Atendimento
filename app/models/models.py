from datetime import datetime
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import MetaData, Table, Column, String, Integer, DateTime, Boolean

Base = declarative_base()

class HealthcareWorker(Base):
    __tablename__ = 'healthcareworker'
    id = Column('', Integer, primary_key=True)
    name = Column('', String(50))
    created = Column('created_on', DateTime, default=datetime.utcnow)

    def retData(self):
        return {'name': self.name}

class Paciente(Base):
    __tablename__ = 'paciente'
    id = Column('', Integer, primary_key=True)
    name = Column('', String(50))
    created = Column('created_on', DateTime, default=datetime.utcnow)

    def retData(self):
        return {'name': self.name}
