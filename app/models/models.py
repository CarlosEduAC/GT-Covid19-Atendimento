from sqlalchemy import Column, String, Integer, DateTime, Date, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy_serializer import SerializerMixin
from datetime import datetime

import base64

Base = declarative_base()

### a partir desta tabela que cadastro no banco
class AdmSaude(Base, SerializerMixin):
    __tablename__ = 'adm_saude'

    idadm_saude = Column('idadm_saude', Integer, primary_key=True)
    nome = Column('nome', String(150))
    crm = Column('crm', String(20))
    cpf = Column('cpf', String(20))
    supervisor = Column('supervisor', String(4))
    senha = Column('senha', String(45))

    def __init__(self, id, nome, crm, cpf, supervisor, senha):
        self.id = id
        self.nome = nome
        self.crm = crm
        self.cpf = cpf
        self.supervisor = supervisor
        self.senha = encode64.b64encode(bytes(str(senha), 'utf-8'))


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