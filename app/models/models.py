from sqlalchemy import Column, String, Integer, DateTime, Date, ForeignKey, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy_serializer import SerializerMixin
from datetime import datetime

import base64

Base = declarative_base()

### a partir desta tabela que cadastro no banco
class AdmSaude(Base, SerializerMixin):
    __tablename__ = 'adm_saude'

    id = Column('idadm_saude', Integer, primary_key=True)
    nome = Column('nome', String(150))
    crm = Column('crm', String(20))
    cpf = Column('cpf', String(20))
    supervisor = Column('supervisor', Boolean)
    senha = Column('senha', String(45))

    def __init__(self, id, nome, crm, cpf, supervisor, senha):
        self.id = id
        self.nome = nome
        self.crm = crm
        self.cpf = cpf
        self.supervisor = supervisor
        self.senha = base64.b64encode(bytes(str(senha), 'utf-8'))


class Paciente(Base, SerializerMixin):
    __tablename__ = 'pacientes'

    nome = Column('nome', String(150, 'utf8_bin'))
    cpf = Column('cpf', Integer)
    sexo = Column('sexo', String(2, 'utf8_bin'))
    raca = Column('raca', String(35, 'utf8_bin'))
    dataNasc = Column('data_nasc', Date)
    id = Column('PacienteId', Integer, primary_key=True)

    def __init__(self, nome, cpf, sexo, raca, dataNasc, id):
        self.id = id
        self.nome = nome
        self.cpf = cpf
        self.sexo = sexo
        self.raca = raca
        self.dataNasc = dataNasc
   
class Comorbidade(Base, SerializerMixin):
    __tablename__ = 'comorbidades'

    idComorbidades = Column(Integer, primary_key=True)
    Descricao = Column(String(150, 'utf8_bin'), nullable=False)

#==================================================
# Tabelas adicionadas para a tela de adm

class EstrategiaSaudeFamiliar(Base, SerializerMixin):
    __tablename__ = 'estrategia_saude_familiar'

    id = Column(Integer, primary_key=True)
    estrategia = Column('estrategia', String(150))

    def __init__(self, estrategia):
        self.estrategia = estrategia

class TemposContatoAcompanhamento(Base, SerializerMixin):
    __tablename__ = 'tempos_contato_acompanhamento'

    id = Column(Integer, primary_key=True)
    intervalo_contato = Column('intervalo_contato', Integer)
    tempo_maximo_acompanhamento = Column('tempo_maximo_acompanhamento', Integer)

    def __init__(self, intervalo_contato, tempo_maximo_acompanhamento):
        self.intervalo_contato = intervalo_contato
        self.tempo_maximo_acompanhamento = tempo_maximo_acompanhamento

#=================================================