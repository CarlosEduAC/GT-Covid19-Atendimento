from sqlalchemy import Column, String, Integer, Float, DateTime, Date, ForeignKey, Boolean, Enum
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

# Tabelas de domínio

class OpcaoTentativa(Base, SerializerMixin):
    __tablename__ = 'opcoesTentativa'

    id = Column('opcoes_tentativa_id', Integer, primary_key=True)
    value = Column('value', String(150, 'utf8_bin'))

    def __init__(self, value):
        self.value = value

class Raca(Base, SerializerMixin):
    __tablename__ = 'racas'

    id = Column('raca_id', Integer, primary_key=True)
    value = Column('value', String(150, 'utf8_bin'))

    def __init__(self, value):
        self.value = value


class Sexo(Base, SerializerMixin):
    __tablename__ = 'sexos'

    id = Column('sexo_id', Integer, primary_key=True)
    value = Column('value', String(150, 'utf8_bin'))

    def __init__(self, value):
        self.value = value


class DoencaCronica(Base, SerializerMixin):
    __tablename__ = 'doencasCronicas'

    id = Column('doenca_cronica_id', Integer, primary_key=True)
    value = Column('value', String(150, 'utf8_bin'))

    def __init__(self, value):
        self.value = value


class Parentesco(Base, SerializerMixin):
    __tablename__ = 'parentescos'

    id = Column('parentesco_id', Integer, primary_key=True)
    value = Column('value', String(150, 'utf8_bin'))

    def __init__(self, value):
        self.value = value


class BeneficioSocial(Base, SerializerMixin):
    __tablename__ = 'beneficiosSociais'

    id = Column('beneficio_social_id', Integer, primary_key=True)
    value = Column('value', String(150, 'utf8_bin'))

    def __init__(self, value):
        self.value = value


class MotivoSair(Base, SerializerMixin):
    __tablename__ = 'motivosSair'

    id = Column('motivo_sair_id', Integer, primary_key=True)
    value = Column('value', String(150, 'utf8_bin'))

    def __init__(self, value):
        self.value = value


class Sintoma(Base, SerializerMixin):
    __tablename__ = 'sintomas'

    id = Column('sintoma_id', Integer, primary_key=True)
    value = Column('value', String(150, 'utf8_bin'))

    def __init__(self, value):
        self.value = value


class SintomaFamiliar(Base, SerializerMixin):
    __tablename__ = 'sintomasFamiliar'

    id = Column('sintoma_familiar_id', Integer, primary_key=True)
    value = Column('value', String(150, 'utf8_bin'))

    def __init__(self, value):
        self.value = value


class IndicadorMedicamento(Base, SerializerMixin):
    __tablename__ = 'indicadoresMedicamento'

    id = Column('indicador_medicamento_id', Integer, primary_key=True)
    value = Column('value', String(150, 'utf8_bin'))

    def __init__(self, value):
        self.value = value


class OrientacaoFinal(Base, SerializerMixin):
    __tablename__ = 'orientacaoFinal'

    id = Column('orientacao_final_id', Integer, primary_key=True)
    value = Column('value', String(150, 'utf8_bin'))

    def __init__(self, value):
        self.value = value

class Esf(Base, SerializerMixin):
    __tablename__ = 'esf'

    id = Column('esf_id', Integer, primary_key=True)
    value = Column('value', String(150, 'utf8_bin'))

    def __init__(self, value):
        self.value = value