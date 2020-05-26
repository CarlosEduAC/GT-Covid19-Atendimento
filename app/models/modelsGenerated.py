# Modelo gerado a partir de um script de banco MySql
# Para tal foi usada esta ferramenta (https://github.com/ksindi/flask-sqlacodegen) a qual é um fork desta outra (https://pypi.org/project/sqlacodegen/). O fork foi realizado para adequação a sintaxe do Flask
# Comando executado: flask-sqlacodegen mysql+pymysql://covid:Covid_UFF_UFRJ@10.77.0.29:3306/atendimento_covid_teste --flask > modelsGenerated.py

# coding: utf-8
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship
from sqlalchemy.schema import FetchedValue
from sqlalchemy import Column, Date, DateTime, ForeignKey, Integer, SmallInteger, String, Table


db = SQLAlchemy()


class AdmSaude(db.Model):
    __tablename__ = 'adm_saude'

    idadm_saude = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(150, 'utf8_bin'))
    CRM = db.Column(db.String(20, 'utf8_bin'), unique=True)
    supervisor = db.Column(db.String(4, 'utf8_bin'), info='verifica se administrador de saue é supervisor (sim/não)')



class Amostra(db.Model):
    __tablename__ = 'amostra'

    amostra_id = db.Column(db.Integer, primary_key=True)
    descricao = db.Column(db.String(45, 'utf8_bin'))



class AmostraColeNotifica(db.Model):
    __tablename__ = 'amostra_cole_notifica'

    idColeta_amostra = db.Column(db.ForeignKey('coleta.idColeta_amostra'), primary_key=True, nullable=False)
    amostra_id = db.Column(db.ForeignKey('amostra.amostra_id'), primary_key=True, nullable=False, index=True)
    idNotificacao = db.Column(db.ForeignKey('notificacao.idNotificacao'), primary_key=True, nullable=False, index=True)

    amostra = db.relationship('Amostra', primaryjoin='AmostraColeNotifica.amostra_id == Amostra.amostra_id', backref='amostra_cole_notificas')
    coleta = db.relationship('Coleta', primaryjoin='AmostraColeNotifica.idColeta_amostra == Coleta.idColeta_amostra', backref='amostra_cole_notificas')
    notificacao = db.relationship('Notificacao', primaryjoin='AmostraColeNotifica.idNotificacao == Notificacao.idNotificacao', backref='amostra_cole_notificas')



class Cidade(db.Model):
    __tablename__ = 'cidade'

    city_id = db.Column(db.SmallInteger, primary_key=True)
    city = db.Column(db.String(50, 'utf8_bin'), nullable=False)
    last_update = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue())



t_classifica_notifica = db.Table(
    'classifica_notifica',
    db.Column('idNotificacao', db.ForeignKey('notificacao.idNotificacao'), index=True),
    db.Column('idClassificacao_final', db.ForeignKey('classificacao_final.idClassificacao_final'), index=True)
)



class ClassificacaoFinal(db.Model):
    __tablename__ = 'classificacao_final'

    idClassificacao_final = db.Column(db.Integer, primary_key=True)
    Descricao = db.Column(db.String(55, 'utf8_bin'))

    notificacao = db.relationship('Notificacao', secondary='classifica_notifica', backref='classificacao_finals')



class Coleta(db.Model):
    __tablename__ = 'coleta'

    idColeta_amostra = db.Column(db.Integer, primary_key=True)
    descricao = db.Column(db.String(45, 'utf8_bin'))
    data_coleta = db.Column(db.Date)
    id_amostra = db.Column(db.Integer)



class Comorbidade(db.Model):
    __tablename__ = 'comorbidades'

    idComorbidades = db.Column(db.Integer, primary_key=True)
    Descricao = db.Column(db.String(150, 'utf8_bin'), nullable=False)



t_comorbidades_pacientes = db.Table(
    'comorbidades_pacientes',
    db.Column('comorbidadeID', db.ForeignKey('comorbidades.idComorbidades'), primary_key=True, nullable=False),
    db.Column('PacienteId', db.ForeignKey('pacientes.PacienteId'), primary_key=True, nullable=False, index=True)
)



class CriterioEncerramento(db.Model):
    __tablename__ = 'criterio_encerramento'

    idCriterio_encerramento = db.Column(db.Integer, primary_key=True)
    Descricao = db.Column(db.String(45, 'utf8_bin'))



class Endereco(db.Model):
    __tablename__ = 'enderecos'

    end_id = db.Column(db.Integer, primary_key=True)
    address = db.Column(db.String(50, 'utf8_bin'))
    bairro = db.Column(db.String(20, 'utf8_bin'))
    city_id = db.Column(db.ForeignKey('cidade.city_id'), nullable=False, index=True)
    postal_code = db.Column(db.String(10, 'utf8_bin'))

    city = db.relationship('Cidade', primaryjoin='Endereco.city_id == Cidade.city_id', backref='enderecoes')



class EvolucaoCaso(db.Model):
    __tablename__ = 'evolucao_caso'

    idevolucao = db.Column(db.Integer, primary_key=True)
    descricao = db.Column(db.String(100, 'utf8_bin'))



class Internacao(db.Model):
    __tablename__ = 'internacao'

    idInternacao = db.Column(db.Integer, primary_key=True)
    UnidadeSaude = db.Column(db.String(45, 'utf8_bin'))
    Data_entrada = db.Column(db.Date)
    Data_saida = db.Column(db.Date)
    CodPaciente = db.Column(db.ForeignKey('pacientes.PacienteId'), index=True)
    UTI = db.Column(db.String(45, 'utf8_bin'))
    CodSuporteVentilatorio = db.Column(db.ForeignKey('suporte_ventilatorio.idsuporte_Ventilatorio'), index=True)
    Criterio_encerramento = db.Column(db.ForeignKey('criterio_encerramento.idCriterio_encerramento'), index=True)
    obito = db.Column(db.String(45, 'utf8_bin'))
    adm_saude = db.Column(db.ForeignKey('adm_saude.idadm_saude'), index=True)

    paciente = db.relationship('Paciente', primaryjoin='Internacao.CodPaciente == Paciente.PacienteId', backref='internacaos')
    suporte_ventilatorio = db.relationship('SuporteVentilatorio', primaryjoin='Internacao.CodSuporteVentilatorio == SuporteVentilatorio.idsuporte_Ventilatorio', backref='internacaos')
    criterio_encerramento = db.relationship('CriterioEncerramento', primaryjoin='Internacao.Criterio_encerramento == CriterioEncerramento.idCriterio_encerramento', backref='internacaos')
    adm_saude1 = db.relationship('AdmSaude', primaryjoin='Internacao.adm_saude == AdmSaude.idadm_saude', backref='internacaos')



class IsolamentDomiciliar(db.Model):
    __tablename__ = 'isolament_domiciliar'

    idisolament_domiciliar = db.Column(db.Integer, primary_key=True)
    descricao = db.Column(db.String(150, 'utf8_bin'), info='dorme no mesmo quarto, dorme na mesma cama, compartilha o mesmo banheiro, compartilha a casa toda, nenhuma das respostas')



class Isolamento(db.Model):
    __tablename__ = 'isolamento'

    idisolamento = db.Column(db.Integer, primary_key=True)
    descricao = db.Column(db.String(150, 'utf8_bin'))



class Notificacao(db.Model):
    __tablename__ = 'notificacao'

    idNotificacao = db.Column(db.Integer, primary_key=True, nullable=False)
    idpac = db.Column(db.ForeignKey('pacientes.PacienteId'), primary_key=True, nullable=False, index=True)
    Datapreencimento = db.Column(db.Date)
    Data_sintomas = db.Column(db.Date)
    id_evolucao_caso = db.Column(db.ForeignKey('evolucao_caso.idevolucao'), index=True)
    adm_saude = db.Column(db.ForeignKey('adm_saude.idadm_saude'), index=True)

    adm_saude1 = db.relationship('AdmSaude', primaryjoin='Notificacao.adm_saude == AdmSaude.idadm_saude', backref='notificacaos')
    evolucao_caso = db.relationship('EvolucaoCaso', primaryjoin='Notificacao.id_evolucao_caso == EvolucaoCaso.idevolucao', backref='notificacaos')
    paciente = db.relationship('Paciente', primaryjoin='Notificacao.idpac == Paciente.PacienteId', backref='notificacaos')



class OutrosMoradore(db.Model):
    __tablename__ = 'outros_moradores'

    id_outros_moradores = db.Column(db.Integer, primary_key=True)
    id_paciente = db.Column(db.ForeignKey('pacientes.PacienteId'), index=True)
    id_notifica = db.Column(db.ForeignKey('notificacao.idNotificacao'), index=True)

    notificacao = db.relationship('Notificacao', primaryjoin='OutrosMoradore.id_notifica == Notificacao.idNotificacao', backref='outros_moradores')
    paciente = db.relationship('Paciente', primaryjoin='OutrosMoradore.id_paciente == Paciente.PacienteId', backref='outros_moradores')



t_pac_end = db.Table(
    'pac_end',
    db.Column('end_id', db.ForeignKey('enderecos.end_id'), primary_key=True, nullable=False),
    db.Column('PacienteId', db.ForeignKey('pacientes.PacienteId'), primary_key=True, nullable=False, index=True)
)



t_paciente_sintomas = db.Table(
    'paciente_sintomas',
    db.Column('idsintomas', db.ForeignKey('sintomas.idsintomas'), index=True),
    db.Column('PacienteId', db.ForeignKey('pacientes.PacienteId'), index=True)
)



class Paciente(db.Model):
    __tablename__ = 'pacientes'

    PacienteId = db.Column(db.Integer, primary_key=True)
    sexo = db.Column(db.String(2, 'utf8_bin'), nullable=False)
    data_nasc = db.Column(db.Date)
    raca = db.Column(db.String(35, 'utf8_bin'))

    comorbidades = db.relationship('Comorbidade', secondary='comorbidades_pacientes', backref='pacientes')
    ends = db.relationship('Endereco', secondary='pac_end', backref='pacientes')
    sintomas = db.relationship('Sintoma', secondary='paciente_sintomas', backref='pacientes')



class Sintoma(db.Model):
    __tablename__ = 'sintomas'

    idsintomas = db.Column(db.Integer, primary_key=True)
    Descricao = db.Column(db.String(100, 'utf8_bin'))

    tele_atendimento = db.relationship('TeleAtendimento', secondary='tele_atendimento_novos_sintomas', backref='sintomas')



class SuporteVentilatorio(db.Model):
    __tablename__ = 'suporte_ventilatorio'

    idsuporte_Ventilatorio = db.Column(db.Integer, primary_key=True)
    descricao = db.Column(db.String(45, 'utf8_bin'))



class TeleAtendimento(db.Model):
    __tablename__ = 'tele_atendimento'

    idteleatendimento = db.Column(db.Integer, primary_key=True)
    adm_saude = db.Column(db.ForeignKey('adm_saude.idadm_saude'), db.ForeignKey('adm_saude.idadm_saude'), index=True)
    atendimento_realizado = db.Column(db.String(4, 'utf8_bin'))
    motivo_falha = db.Column(db.String(45, 'utf8_bin'))
    novos_sintomas = db.Column(db.String(4, 'utf8_bin'))
    medicacao = db.Column(db.String(150, 'utf8_bin'))
    indicacao_medicacao = db.Column('indicacao medicacao', db.String(45, 'utf8_bin'))
    teleatendimentocol = db.Column(db.String(45, 'utf8_bin'))
    tem_outros_moradores = db.Column(db.String(45, 'utf8_bin'))
    fazendo_isolamento = db.Column(db.String(45, 'utf8_bin'))
    tipo_isolamento = db.Column(db.ForeignKey('isolamento.idisolamento'), index=True)
    tem_trabalho_externo = db.Column(db.String(45, 'utf8_bin'))
    tipo_trabalho = db.Column(db.String(45, 'utf8_bin'))
    dias_isolamento = db.Column(db.Integer)
    situacao_familiar = db.Column(db.String(45, 'utf8_bin'), info='tipo de situação:  sai para trabalho essencial apenas, sai somente para atvidades essenciais , sai para atividades não essenciais 9exercicios, visitas familiares, etc)')
    mora_sozinho = db.Column(db.String(4, 'utf8_bin'))
    tele_atendimentocol = db.Column(db.String(45, 'utf8_bin'))
    iso_domiciliar = db.Column(db.ForeignKey('isolament_domiciliar.idisolament_domiciliar'), index=True)
    outro_morador_sintomas = db.Column(db.String(4, 'utf8_bin'))
    data_atendimento = db.Column(db.Date)
    data_proximo_atendimento = db.Column(db.Date)
    adm_supervisor = db.Column(db.Integer)
    adm_tele = db.Column(db.String(4, 'utf8_bin'))

    adm_saude1 = db.relationship('AdmSaude', primaryjoin='TeleAtendimento.adm_saude == AdmSaude.idadm_saude', backref='admsaude_tele_atendimentoes')
    adm_saude2 = db.relationship('AdmSaude', primaryjoin='TeleAtendimento.adm_saude == AdmSaude.idadm_saude', backref='admsaude_tele_atendimentoes_0')
    isolament_domiciliar = db.relationship('IsolamentDomiciliar', primaryjoin='TeleAtendimento.iso_domiciliar == IsolamentDomiciliar.idisolament_domiciliar', backref='tele_atendimentoes')
    isolamento = db.relationship('Isolamento', primaryjoin='TeleAtendimento.tipo_isolamento == Isolamento.idisolamento', backref='tele_atendimentoes')



t_tele_atendimento_novos_sintomas = db.Table(
    'tele_atendimento_novos_sintomas',
    db.Column('id_tele', db.ForeignKey('tele_atendimento.idteleatendimento'), primary_key=True, nullable=False),
    db.Column('id_sintomas_novos', db.ForeignKey('sintomas.idsintomas'), primary_key=True, nullable=False, index=True)
)
