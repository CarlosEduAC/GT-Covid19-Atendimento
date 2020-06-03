from sqlalchemy import Column, String, Integer, DateTime, ForeignKey, Boolean
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()

class Agendamento(Base):

    __tablename__ = 'agendamento'
    
    dia = Column('dia', DateTime)
    idProfissional = Column('idProfissional', Integer, ForeignKey('profissional_saude.idProfissional'))
    idAtendimento = Column('idAtendimento', Integer, ForeignKey('atendimento.idAtendimento'))
    idUsuario = Column('idUsuario', Integer, ForeignKey('usuario.idUsuario'))
    id = Column('idAgendamento', Integer, primary_key = True)


class ProfissionalSaude(Base):

    __tablename__ = 'profissional_saude'

    id = Column('idProfissional', Integer, primary_key = True)

class Atendimento(Base):

    __tablename__ = 'atendimento'

    primeiro = Column('primeiro', Boolean)
    dia = Column('dia', DateTime)
    id = Column('idAtendimento', Integer, primary_key = True)





