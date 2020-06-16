from sqlalchemy import Column, String, Integer, DateTime, Date, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy_serializer import SerializerMixin
from datetime import datetime

Base = declarative_base()

### a partir desta tabela que cadastro no banco
class AdmSaude(Base, SerializerMixin):
    __tablename__ = 'adm_saude'

    idadm_saude = Column('idadm_saude', Integer, ForeignKey('usuario.idUsuario'), primary_key=True)
    nome = Column('nome', String(50))
    CRM = Column('crm', String(20), unique=True)
    supervisor = Column('supervisor', String(4))

    def __init__(self, nome, crm, cargo, id):
        self.nome = nome
        self.CRM = crm
        self.supervisor = cargo
        self.idadm_saude = id

class Usuario(Base, SerializerMixin):
    __tablename__ = 'usuario'
    name = Column('nome', String(50))
    cpf = Column('cpf', String(16))
    crm = Column('crm', String(20))
    senha = Column('senha', String(16))
    created = Column('created_on', DateTime, default=datetime.utcnow)
    id = Column('idUsuario', Integer, primary_key=True)

    #usuarioPerfil = relationship("UsuarioPerfil")

    def __init__(self, name, cpf, crm, senha):
        self.name = name
        self.cpf = cpf
        self.crm = crm
        self.senha = senha

class UsuarioPerfil(Base, SerializerMixin):
    __tablename__ = 'usuario_perfil'  
    idUsuario = Column('idUsuario', Integer, ForeignKey('usuario.idUsuario'), primary_key=True)
    idPerfil = Column('idPerfil', Integer, ForeignKey('perfil.idPerfil'), primary_key=True)

class Paciente(Base, SerializerMixin):
    __tablename__ = 'pacientes'

    nome = Column('nome', String(150, 'utf8_bin'))
    cpf = Column('cpf', Integer)
    sexo = Column('sexo', String(2, 'utf8_bin'))
    raca = Column('raca', String(35, 'utf8_bin'))
    dataNasc = Column('data_nasc', Date)
    id = Column('PacienteId', Integer, primary_key=True)

    def __repr__(self):
        return f'Paciente {self.name, self.cpf, self.sexo, self.raca, self.dataNasc}' 

class Comorbidade(Base, SerializerMixin):
    __tablename__ = 'comorbidades'

    idComorbidades = Column(Integer, primary_key=True)
    Descricao = Column(String(150, 'utf8_bin'), nullable=False)