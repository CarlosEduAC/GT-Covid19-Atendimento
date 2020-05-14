from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import MetaData, Table, Column, String, Integer, DateTime, Boolean
from sqlalchemy.orm import relationship
from datetime import datetime

Base = declarative_base()

class User(Base):
    __tablename__ = 'referee'
    name = Column('ref_nm_name', String(50))
    created = Column('ref_created_on', DateTime, default=datetime.utcnow)
    id = Column('ref_nr_id', Integer, primary_key=True)

    def retData(self):
        return {'name': self.name}

class Commission(Base):
    __tablename__ = 'commission'
    name = Column('com_nm_name', String(50))
    created = Column('com_created_on', DateTime, default=datetime.utcnow)
    role = Column('com_ds_role', String(50))
    id = Column('com_nr_id', Integer, primary_key=True)

    def retData(self):
        return {'name': self.name, 'role': self.role}
