import re
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy import Column, Date, DateTime, ForeignKey, String
from sqlalchemy.dialects.mysql import INTEGER, TINYINT
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy_serializer import SerializerMixin
from flask_login import UserMixin

Base = declarative_base()


class AdmSaude(Base, SerializerMixin, UserMixin):
    __tablename__ = 'adms_saude'

    id = Column(INTEGER(11), primary_key=True)
    nome = Column(String(150), nullable=False)
    crm = Column(String(20))
    cpf = Column(String(11))
    is_supervisor = Column(TINYINT(4), nullable=False)
    senha = Column(String(150), nullable=False)

    def __init__(self, nome, crm, cpf, is_supervisor, senha=None):
        self.nome = nome
        self.crm = crm
        self.cpf = cpf
        self.is_supervisor = is_supervisor
        if senha is not None:
            self.senha = generate_password_hash(senha)

    def verificaSenha(self, senha):
        return check_password_hash(self.senha, senha)

    def validarCPF(self):
        if not self.cpf:
            return False

        num_cpf = self.calculoCPF(self.cpf[:9])
        num_cpf = self.calculoCPF(num_cpf)

        if num_cpf == self.cpf:
            return True
        return False

    # gera cpf válido a partir do cpf que foi dado como input
    def calculoCPF(self, num_cpf):
        if not num_cpf:
            return False

        seq = num_cpf[0] * len(num_cpf)

        if seq == num_cpf:
            return False

        soma = 0
        for ch, mult in enumerate(range(len(num_cpf) + 1, 1, -1)):
            soma += int(num_cpf[ch]) * mult

        res = 11 - (soma % 11)
        res = res if res <= 9 else 0

        return num_cpf + str(res)


class AtendimentoInicial(Base, SerializerMixin):
    __tablename__ = 'atendimentos_iniciais'

    id = Column(INTEGER(11), primary_key=True)
    endereco = Column(String(255))
    qnt_comodos = Column(INTEGER(11))
    is_agua_encanada = Column(TINYINT(4))


class Paciente(Base, SerializerMixin):
    __tablename__ = 'pacientes'

    id = Column(INTEGER(11), primary_key=True)
    nome = Column(String(150), nullable=False)
    cpf = Column(String(11), nullable=False)
    telefone = Column(String(11), nullable=False)
    endereco = Column(String(255), nullable=False)
    data_nasc = Column(Date)
    id_etnia = Column(ForeignKey('etnias.id'), index=True)
    id_genero = Column(ForeignKey('generos.id'), index=True)

    etnia = relationship('Etnia')
    genero = relationship('Genero')

    def __init__(self, nome, cpf, telefone, data_nasc, id_etnia, id_genero, endereco):
        self.nome = nome
        self.cpf = cpf
        self.telefone = telefone
        self.data_nasc = data_nasc
        self.id_etnia = id_etnia
        self.id_genero = id_genero
        self.endereco = endereco


class Atendimento(Base, SerializerMixin):
    __tablename__ = 'atendimentos'

    id = Column(INTEGER(11), primary_key=True)
    # id_inicial = Column(INTEGER(11)) Aparentemente, o id do atendimento inicial estava duplicado
    id_atendimento_inicial = Column(ForeignKey('atendimentos_iniciais.id'), index=True)
    id_paciente = Column(ForeignKey('pacientes.id'), nullable=False, index=True)
    is_primeiro = Column(TINYINT(4), nullable=False)
    data = Column(DateTime, nullable=False)

    # --se nao conseguir realizar o atendimento--#
    id_tentativa = Column(ForeignKey('tentativas.id'), index=True)
    outras_tentativas = Column(String(255))

    # --dados isolamento--#
    cuidado_sair_casa = Column(String(255))

    consegue_isolamento = Column(TINYINT(4))
    como_consegue = Column(String(255))
    porque_nao_consegue = Column(String(255))

    consegue_ficar_casa = Column(TINYINT(4))
    quantos_dias = Column(INTEGER(11))
    # ------------------------#

    atendimentos_iniciai = relationship('AtendimentoInicial')
    paciente = relationship('Paciente')
    tentativa = relationship('Tentativa')


class Agendamento(Base, SerializerMixin):
    __tablename__ = 'agendamentos'

    id = Column(INTEGER(11), primary_key=True)
    id_adm_saude = Column(ForeignKey('adms_saude.id'), nullable=False, index=True)
    id_atendimento = Column(ForeignKey('atendimentos.id'), index=True)
    id_paciente = Column(ForeignKey('pacientes.id'), nullable=False, index=True)
    data = Column(DateTime, nullable=False)

    adms_saude = relationship('AdmSaude')
    atendimento = relationship('Atendimento')
    paciente = relationship('Paciente')


class TempoContatoAcompanhamento(Base, SerializerMixin):
    __tablename__ = 'tempos_contato_acompanhamento'

    id = Column(INTEGER(11), primary_key=True)
    intervalo_contato = Column('intervalo_contato', INTEGER(11))
    tempo_maximo_acompanhamento = Column('tempo_maximo_acompanhamento', INTEGER(11))

    def __init__(self, intervalo_contato, tempo_maximo_acompanhamento):
        self.intervalo_contato = intervalo_contato
        self.tempo_maximo_acompanhamento = tempo_maximo_acompanhamento
