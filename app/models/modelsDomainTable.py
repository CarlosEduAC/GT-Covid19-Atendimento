from sqlalchemy import Column, String
from sqlalchemy.dialects.mysql import INTEGER
from sqlalchemy_serializer import SerializerMixin
from models.models import Base


# Tabelas de domínio

class BeneficioSocial(Base, SerializerMixin):
    __tablename__ = 'beneficios_sociais'

    id = Column(INTEGER(11), primary_key=True)
    value = Column(String(150), nullable=False)

    def __init__(self, value):
        self.value = value


class DoencaCronica(Base, SerializerMixin):
    __tablename__ = 'doencas_cronicas'

    id = Column(INTEGER(11), primary_key=True)
    value = Column(String(150), nullable=False)

    def __init__(self, value):
        self.value = value


class EstrategiaSaudeFamiliar(Base, SerializerMixin):
    __tablename__ = 'estrategias_saude_familiar'

    id = Column(INTEGER(11), primary_key=True)
    value = Column(String(150), nullable=False)

    def __init__(self, value):
        self.value = value


class Etnia(Base, SerializerMixin):
    __tablename__ = 'etnias'

    id = Column(INTEGER(11), primary_key=True)
    value = Column(String(150), nullable=False)

    def __init__(self, value):
        self.value = value


class Genero(Base, SerializerMixin):
    __tablename__ = 'generos'

    id = Column(INTEGER(11), primary_key=True)
    value = Column(String(150), nullable=False)

    def __init__(self, value):
        self.value = value


class Indicador(Base, SerializerMixin):
    __tablename__ = 'indicadores'

    id = Column(INTEGER(11), primary_key=True)
    value = Column(String(150), nullable=False)

    def __init__(self, value):
        self.value = value


class Medicamento(Base, SerializerMixin):
    __tablename__ = 'medicamentos'

    id = Column(INTEGER(11), primary_key=True)
    value = Column(String(150), nullable=False)

    def __init__(self, value):
        self.value = value


class MotivoSair(Base, SerializerMixin):
    __tablename__ = 'motivos_sair'

    id = Column(INTEGER(11), primary_key=True)
    value = Column(String(150), nullable=False)

    def __init__(self, value):
        self.value = value


class OrientacaoFinal(Base, SerializerMixin):
    __tablename__ = 'orientacoes_finais'

    id = Column(INTEGER(11), primary_key=True)
    value = Column(String(150), nullable=False)

    def __init__(self, value):
        self.value = value


class Parentesco(Base, SerializerMixin):
    __tablename__ = 'parentescos'

    id = Column(INTEGER(11), primary_key=True)
    value = Column(String(150), nullable=False)

    def __init__(self, value):
        self.value = value


class Sintoma(Base, SerializerMixin):
    __tablename__ = 'sintomas'

    id = Column(INTEGER(11), primary_key=True)
    value = Column(String(150), nullable=False)

    def __init__(self, value):
        self.value = value


class Tentativa(Base, SerializerMixin):
    __tablename__ = 'tentativas'

    id = Column(INTEGER(11), primary_key=True)
    value = Column(String(150), nullable=False)

    def __init__(self, value):
        self.value = value
