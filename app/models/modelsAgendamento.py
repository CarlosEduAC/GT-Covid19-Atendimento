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
# class Comorbidade(Base):
#     __tablename__ = 'comorbidade'

#     id = Column('id', Integer, primary_key=True)
#     idAtendimento = Column('idAtendimento', Integer, ForeignKey(AtendimentoInicial.id))

#     dataPrimeiroSintoma = Column('dataPrimeiroSintoma', DateTime)
#     comorbidade = Column('comorbidade', String) #Vai virar um Enum?
#                                                 #Se não, precisaremos de tabela comorbidades?

# Doenca Cronica

class DoencaCronicaAtendimento(Base):
    __tablename__ = 'doencasCronicasAtendimento'
    
    id = Column('id', Integer, primary_key=True)
    idAtendimento = Column('idAtendimento', Integer, ForeignKey('atendimento.id'))
    idDoencaCronica = Column('idDoencaCronica', Integer, ForeignKey('doencasCronicas.id'))


# Medicamento
class MedicamentoAtendimento(Base):
    __tablename__ = 'medicamentoAtendimento'

    id = Column('id', Integer, primary_key=True)
    idAtendimento = Column('idAtendimento', Integer, ForeignKey('atendimento.id'))
    idMedicamento = Column('idMedicamento', Integer, ForeignKey('medicamentos.id'))
    idIndicador = Column('idIndicador', Integer, ForeignKey('indicadoresMedicamento.id'))

    doseRemedioPaciente = Column('dose', String)
    tmpRemedioPaciente = Column('tempo', String)
    indicouRemedioPaciente = Column('indicou', Boolean)


class BeneficioSocialAtendimento(Base):
    __tablename__ = 'beneficiosSociaisAtendimento'

    id = Column('id', Integer, primary_key=True)
    idAtendimento = Column('idAtendimento', Integer, ForeignKey(AtendimentoInicial.id))
    idBeneficioSocial = Column('idBeneficioSocial', Integer, ForeignKey('beneficiosSociais.id'))


class MotivosSairAtendimento(Base):
    __tablename__ = 'motivosSairAtendimento'

    id = Column('id', Integer, primary_key=True)
    idAtendimento = Column('idAtendimento', Integer, ForeignKey(Atendimento.id))
    idMotivosSairDeCasa = Column('idMotivosSairDeCasa', Integer, ForeignKey("motivosSair.id"))

class SintomaAtendimento(Base):
    __tablename__ = 'sintomasAtendimento'

    id = Column('id', Integer, primary_key=True)
    idAtendimento = Column('idAtendimento', Integer, ForeignKey(Atendimento.id))
    idSintoma = Column('idSintoma', ForeignKey("sintomas.id"))


class MedicamentoSintomasAtendimento(Base):
    __tablename__ = 'medicamentoSintomasAtendimento'

    id = Column('id', Integer, primary_key=True)
    idAtendimento = Column('idAtendimento', Integer, ForeignKey('atendimento.id'))
    idMedicamento = Column('idMedicamento', Integer, ForeignKey('medicamentos.id'))
    idIndicador = Column('idIndicador', Integer, ForeignKey('indicadoresMedicamento.id'))

    doseRemedioPaciente = Column('dose', String)
    tmpRemedioPaciente = Column('tempo', String)
    indicouRemedioPaciente = Column('indicou', Boolean)


class SintomasCovidFamiliar(Base): #Da pra misturar na tabela Sintomas acima? 
                                   # Mesmo problema da tabela DoencaCronicaPessoa
    __tablename__ = 'sintomas_covid_familiar'
    
    id = Column('id', Integer, primary_key=True)
    idPessoa = Column('idPessoa', Integer, ForeignKey(FamiliarDoencaCronicaAtendimento.id))

    sintomaCovid19Field = Column('sintomaCovid19Field', Enum(Sintomas))
    seFebreDeQuanto = Column('seFebreDeQuanto', Float)


class OrientacaoFinal(Base):
    __tablename__ = 'orientacao_final'

    id = Column('id', Integer, primary_key=True)
    idAtendimento = Column('idAtendimento', Integer, ForeignKey(Atendimento.id))

    outroAtendimentoField = Column('outroAtendimentoField', Enum(OrientacaoFinal))

class FamiliarDoencaCronicaAtendimento(Base):
    __tablename__ = 'familiarDoencasCronicas'

    id = Column('id', Integer, primary_key=True)
    idAtendimento = Column('idAtendimento', Integer, ForeignKey(Atendimento.id))

    familiarDoencaCronica = Column('idDoencaCronica', Integer, ForeignKey('doencasCronicas.id'))