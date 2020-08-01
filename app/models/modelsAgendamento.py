from sqlalchemy import Column, ForeignKey, String, DateTime
from sqlalchemy.dialects.mysql import INTEGER, TINYINT
from sqlalchemy.orm import relationship
from sqlalchemy_serializer import SerializerMixin
from models.models import Base


class AtendimentoBeneficioSocial(Base, SerializerMixin):
    __tablename__ = 'atendimentos_beneficios_sociais'

    # id_atendimento_beneficio_sociai = Column(INTEGER(11), primary_key=True)
    id = Column(INTEGER(11), primary_key=True)
    id_atendimento = Column(ForeignKey('atendimentos.id'), nullable=False, index=True)
    id_beneficio_social = Column(ForeignKey('beneficios_sociais.id'), index=True)
    outros_beneficios_sociais = Column(String(150))

    atendimento = relationship('Atendimento')
    beneficios_sociai = relationship('BeneficioSocial')


""" class AtendimentoDoencaCronica(Base, SerializerMixin):
    __tablename__ = 'atendimentos_doencas_cronicas'

    #id_atendimento_doenca_cronica = Column(INTEGER(11), primary_key=True)
    id = Column(INTEGER(11), primary_key=True)
    id_atendimento = Column(ForeignKey('atendimentos.id'), nullable=False, index=True)
    id_doenca_cronica = Column(ForeignKey('doencas_cronicas.id'), index=True)
    id_medicamento = Column(ForeignKey('medicamentos.id'), index=True)
    id_indicador = Column(ForeignKey('indicadores.id'), index=True)
    #id_parentesco = Column(ForeignKey('parentescos.id'), index=True)
    data_sintomas = Column(DateTime, nullable=False)

    outros_medicamentos = Column(String(150))
    outros_indicadores = Column(String(150))
    outras_doencas_cronicas = Column(String(150))

    atendimento = relationship('Atendimento')
    doencas_cronica = relationship('DoencaCronica')
    indicadore = relationship('Indicador')
    medicamento = relationship('Medicamento')
    #parentesco = relationship('Parentesco') """


class AtendimentoEstrategiasSaudesFamiliar(Base, SerializerMixin):
    __tablename__ = 'atendimentos_estrategias_saudes_familiar'

    # id_atendimento_estrategia_saude_familiar = Column(INTEGER(11), primary_key=True)
    id = Column(INTEGER(11), primary_key=True)
    id_atendimento = Column(ForeignKey('atendimentos.id'), nullable=False, index=True)
    id_estrategia_saude_familiar = Column(ForeignKey('estrategias_saude_familiar.id'), index=True)
    outras_estrategias_saude_familiar = Column(String(150))

    atendimento = relationship('Atendimento')
    estrategias_saude_familiar = relationship('EstrategiaSaudeFamiliar')


class AtendimentoMotivoSair(Base, SerializerMixin):
    __tablename__ = 'atendimentos_motivos_sair'

    # id_atendimento_motivo_sair = Column(INTEGER(11), primary_key=True)
    id = Column(INTEGER(11), primary_key=True)
    id_atendimento = Column(ForeignKey('atendimentos.id'), nullable=False, index=True)
    id_motivo_sair = Column(ForeignKey('motivos_sair.id'), index=True)
    outros_motivos_sair = Column(String(150))

    atendimento = relationship('Atendimento')
    motivos_sair = relationship('MotivoSair')


class AtendimentoOrientacaoFinal(Base, SerializerMixin):
    __tablename__ = 'atendimentos_orientacoes_finais'

    # id_atendimento_orientacao_final = Column(INTEGER(11), primary_key=True)
    id = Column(INTEGER(11), primary_key=True)
    id_atendimento = Column(ForeignKey('atendimentos.id'), nullable=False, index=True)
    id_orientacao_final = Column(ForeignKey('orientacoes_finais.id'), index=True)
    comentario = Column(String(255))
    outras_orientacoes_finais = Column(String(150))

    atendimento = relationship('Atendimento')
    orientacoes_finai = relationship('OrientacaoFinal')


""" class AtendimentoSintoma(Base, SerializerMixin):
    __tablename__ = 'atendimentos_sintomas'

    #id_atendimento_sintoma = Column(INTEGER(11), primary_key=True)
    id = Column(INTEGER(11), primary_key=True)
    id_atendimento = Column(ForeignKey('atendimentos.id'), nullable=False, index=True)
    id_sintoma = Column(ForeignKey('sintomas.id'), index=True)
    id_doenca_cronica = Column(ForeignKey('doencas_cronicas.id'), index=True)
    id_parentesco = Column(ForeignKey('parentescos.id'), index=True) #Adicionar campo, adicionar "Mulher grávida"
    #id_medicamento = Column(ForeignKey('medicamentos.id'), index=True) #Vai virar string (alterar campo)
    id_indicador = Column(ForeignKey('indicadores.id'), index=True)

    medicamento = Column(String(150)) #novo campo
    dosagem = Column(String(150))
    data_sintomas = Column(DateTime) #novo campo
    is_mulher_gravida = Column(TINYINT(4)) # novo campo

    outros_sintomas = Column(String(150))
    outras_doencas_cronicas = Column(String(150)) #novo campo

    atendimento = relationship('Atendimento')
    indicadore = relationship('Indicador')
    #medicamento = relationship('Medicamento')
    parentesco = relationship('Parentesco')
    sintoma = relationship('Sintoma')
    doencas_cronica = relationship('DoencaCronica') """


class AtendimentoRelacao(Base, SerializerMixin):
    __tablename__ = 'atendimentos_relacao'

    # id_atendimento_sintoma = Column(INTEGER(11), primary_key=True)
    id = Column(INTEGER(11), primary_key=True)
    id_atendimento = Column(ForeignKey('atendimentos.id'), nullable=False, index=True)
    id_sintoma = Column(ForeignKey('sintomas.id'), index=True)
    id_doenca_cronica = Column(ForeignKey('doencas_cronicas.id'), index=True)
    id_parentesco = Column(ForeignKey('parentescos.id'), index=True)  # Adicionar campo, adicionar "Mulher grávida"
    # id_medicamento = Column(ForeignKey('medicamentos.id'), index=True) #Vai virar string (alterar campo)
    id_indicador = Column(ForeignKey('indicadores.id'), index=True)

    medicamento = Column(String(150))  # novo campo
    dosagem = Column(String(150))
    data_sintomas = Column(DateTime)  # novo campo
    is_mulher_gravida = Column(TINYINT(4))  # novo campo

    outros_sintomas = Column(String(150))
    outras_doencas_cronicas = Column(String(150))  # novo campo

    atendimento = relationship('Atendimento')
    indicadore = relationship('Indicador')
    # medicamento = relationship('Medicamento')
    parentesco = relationship('Parentesco')
    sintoma = relationship('Sintoma')
    doencas_cronica = relationship('DoencaCronica')


class AtendimentoVisita(Base, SerializerMixin):
    __tablename__ = 'atendimentos_visitas'

    # id_atendimento_visita = Column(INTEGER(11), primary_key=True)
    id = Column(INTEGER(11), primary_key=True)
    id_atendimento = Column(ForeignKey('atendimentos.id'), nullable=False, index=True)
    quem_visitou = Column(String(150))
    porque_visitou = Column(String(150))

    atendimento = relationship('Atendimento')

# =========================================================================================
