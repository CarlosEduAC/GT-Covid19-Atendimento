from sqlalchemy import Column, String, Integer, DateTime, ForeignKey, Boolean
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
from models.models import Usuario, Paciente

Base = declarative_base()

class Agendamento(Base):

    __tablename__ = 'agendamento'
    
    dia = Column('dia', DateTime)
    idProfissional = Column('idProfissional', Integer, ForeignKey(Usuario.id))
    idAtendimento = Column('idAtendimento', Integer, ForeignKey('atendimento.idAtendimento'))
    idUsuario = Column('idUsuario', Integer, ForeignKey(Paciente.id))
    id = Column('idAgendamento', Integer, primary_key = True)


class Atendimento(Base):

    __tablename__ = 'atendimento'

    primeiro = Column('primeiro', Boolean)
    dia = Column('dia', DateTime)
    id = Column('idAtendimento', Integer, primary_key = True)





