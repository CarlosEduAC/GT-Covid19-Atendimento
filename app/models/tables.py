from sqlalchemy import Column, String, Integer, DateTime, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()

class Usuario(Base):
    __tablename__ = 'usuario'
    name = Column('nome', String(50))
    cpf = Column('cpf', String(16))
    crm = Column('crm', String(20))
    senha = Column('senha', String(16))
    created = Column('created_on', DateTime, default=datetime.utcnow)
    id = Column('idUsuario', Integer, primary_key=True)

    def __init__(self, name, cpf, crm, senha):
        self.name = name
        self.cpf = cpf
        self.crm = crm
        self.senha = senha

class UsuarioPerfil(Base):
    __tablename__ = 'usuario_perfil'  
    idUsuario = Column('idUsuario', Integer, ForeignKey('usuario.idUsuario'), primary_key=True)
    idPerfil = Column('idPerfil', Integer, ForeignKey('perfil.idPerfil'), primary_key=True)

class Paciente(Base):
    __tablename__ = 'pacientes'
    name = Column('nome', String(50))
    cpf = Column('cpf', String(16))
    ocupacao = Column('ocupacao', String(50))
    sexo = Column('sexo', String(2))
    raca = Column('raca', String(35))
    dataNasc = Column('data_nasc', DateTime)
    created = Column('created_on', DateTime, default=datetime.utcnow)
    id = Column('PacienteId', Integer, primary_key=True)

    def __init__(self, name, cpf, ocupacao, sexo, raca, dataNasc):
        self.name = name
        self.cpf = cpf
        self.ocupacao = ocupacao
        self.sexo = sexo
        self.raca = raca
        self.dataNasc = dataNasc
