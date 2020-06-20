from sqlalchemy import Column, String, Integer, Enum, Float, DateTime, ForeignKey, Boolean
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
from models.models import Atendimento, AtendimentoInicial, IndicadorMedicamento, BeneficiosSociais, DoencasCronicas, Parentesco, Sintomas

Base = declarative_base()

# Aqui estão todas as tabelas para campos com valores Enum/com múltiplas opções.

# A ideia é que precisemos só da tabela que relaciona o item ao atendimento.
# Como são Enums, não precisamos de tabelas específicas pra eles. Ou seja, ao invés de termos:
# Atendimento -> AtendimentoDoenca -> Doenca
# Só precisamos de:
# Atendimento -> Doenca
# Todas as tabelas possuem o id do Atendimento/AtendimentoInicial para conseguirmos consultar.

# ------ Tabelas Relacionadas Primeiro Atendimento ----------------------------
class Comorbidade(Base):
    __tablename__ = 'comorbidade'

    id = Column('id', Integer, primary_key=True)
    idAtendimento = Column('idAtendimento', Integer, ForeignKey(AtendimentoInicial.id))

    dataPrimeiroSintoma = Column('dataPrimeiroSintoma', DateTime)
    comorbidade = Column('comorbidade', String) #Vai virar um Enum?
                                                #Se não, precisaremos de tabela comorbidades?


class DoencaCronica(Base):
    __tablename__ = 'doenca_cronica'

    id = Column('id', Integer, primary_key=True)
    idAtendimento = Column('idAtendimento', Integer, ForeignKey(AtendimentoInicial.id))

    doenca = Column('doenca', Enum(DoencasCronicas))


class Medicamento(Base):
    __tablename__ = 'medicamento'

    id = Column('id', Integer, primary_key=True)
    idAtendimento = Column('idAtendimento', Integer, ForeignKey(AtendimentoInicial.id))

    nome = Column('nome', String) #Vai virar um Enum? Se não, criar tabela para medicamento.
    doseRemedioPaciente = Column('dose', String)
    tmpRemedioPaciente = Column('tempo', String)
    indicouRemedioPaciente = Column('indicou', Boolean)
    quemIndicouRemedioPaciente = Column('quem_indicou', Enum(IndicadorMedicamento))


class Auxilio(Base):
    __tablename__ = 'auxilio'

    id = Column('id', Integer, primary_key=True)
    idAtendimento = Column('idAtendimento', Integer, ForeignKey(AtendimentoInicial.id))

    nome = Column('nome', Enum(BeneficiosSociais))


# ---- Tabelas Relacionadas Atendimento Seguinte
# Essa tabela é uma tabela de doença cronica especifica para a PessoaDomicilio.
# É possível "misturar" com a tabela DoencaCronica acima para não precisarmos de 
# mais de uma tabela de doencacronica?
class DoencaCronicaPessoa(Base): #Para a tabela PessoaDomicilio abaixo
    __tablename__ = 'doenca_cronica_pessoa'

    id = Column('id', Integer, primary_key=True)
    idPessoa = Column('idPessoa', Integer, ForeignKey(PessoaDomicilio.id))

    doenca = Column('doenca', Enum(DoencasCronicas))

class PessoaDomicilio(Base):
    __tablename__ = 'pessoa_domicilio'

    id = Column('id', Integer, primary_key=True)
    idAtendimento = Column('idAtendimento', Integer, ForeignKey(Atendimento.id))

    qualRelacao = Column('qualRelacao', Enum(Parentesco))
    familiarDoencaCronica = Column('familiarDoencaCronica', Boolean)
    # quaisDoencasCronicas = Column('quaisDoencasCronicas', Enum(DoencasCronicas))
    mulherGravida = Column('mulherGravida', Boolean)
    nomeMulheresGravidas = Column('nomeMulheresGravidas', String)


class MotivosSair(Base):
    __tablename__ = 'motivos_sair'

    id = Column('id', Integer, primary_key=True)
    idAtendimento = Column('idAtendimento', Integer, ForeignKey(Atendimento.id))

    motivosSairDeCasaField = Column('motivosSairDeCasaField', Enum(MotivosSair))

class SintomasCovid(Base):
    __tablename__ = 'sintomas_covid'

    id = Column('id', Integer, primary_key=True)
    idAtendimento = Column('idAtendimento', Integer, ForeignKey(Atendimento.id))

    sintomaCovid19Field = Column('sintomaCovid19Field', Enum(Sintomas))


class MedicamentoSintomas(Base):
    __tablename__ = 'medicamento_sintomas'

    id = Column('id', Integer, primary_key=True)
    idAtendimento = Column('idAtendimento', Integer, ForeignKey(Atendimento.id))

    qualMedicamentoTomou = Column('qualMedicamentoTomou', String)
    quemIndicouMedicamento = Column('quemIndicouMedicamento', Enum(IndicadorMedicamento))
    quemIndicouField = Column('quemIndicouField', String) #Para campo "outros"
    comoTomaMedicamento = Column('comoTomaMedicamento', String)


class SintomasCovidFamiliar(Base): #Da pra misturar na tabela Sintomas acima? 
                                   # Mesmo problema da tabela DoencaCronicaPessoa
    __tablename__ = 'sintomas_covid_familiar'
    
    id = Column('id', Integer, primary_key=True)
    idPessoa = Column('idPessoa', Integer, ForeignKey(PessoaDomicilio.id))

    sintomaCovid19Field = Column('sintomaCovid19Field', Enum(Sintomas))
    seFebreDeQuanto = Column('seFebreDeQuanto', Float)


class OrientacaoFinal(Base):
    __tablename__ = 'orientacao_final'

    id = Column('id', Integer, primary_key=True)
    idAtendimento = Column('idAtendimento', Integer, ForeignKey(Atendimento.id))

    outroAtendimentoField = Column('outroAtendimentoField', Enum(OrientacaoFinal))