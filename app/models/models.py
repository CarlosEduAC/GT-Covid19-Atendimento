from sqlalchemy import Column, String, Integer, Float, DateTime, Date, ForeignKey, Boolean, Enum
from sqlalchemy.ext.declarative import declarative_base
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy_serializer import SerializerMixin
from flask_login import \
    UserMixin  # userMinx me permite herdar os metodos is_authenticated e os outros que flask login exige que tenha
from datetime import datetime

import base64

Base = declarative_base()


### a partir desta tabela que cadastro no banco
class AdmSaude(Base, SerializerMixin, UserMixin):
    __tablename__ = 'adm_saude'

    id = Column('idadm_saude', Integer, primary_key=True)
    nome = Column('nome', String(150))
    crm = Column('crm', String(20))
    cpf = Column('cpf', String(20))
    supervisor = Column('supervisor', Boolean)
    senha = Column('senha', String(45))

    def __init__(self, nome, crm, cpf, supervisor, senha):
        self.nome = nome
        self.crm = crm
        self.cpf = cpf
        self.supervisor = supervisor
        self.senha = generate_password_hash(senha)

    def verificaSenha(self, senha):
        return check_password_hash(self.senha, senha)


class Paciente(Base, SerializerMixin):
    __tablename__ = 'pacientes'

    nome = Column('nome', String(150, 'utf8_bin'))
    cpf = Column('cpf', Integer)
    sexo = Column('sexo', String(2, 'utf8_bin'))
    raca = Column('raca', String(35, 'utf8_bin'))
    dataNasc = Column('data_nasc', Date)
    id = Column('PacienteId', Integer, primary_key=True)

    def __init__(self, nome, cpf, sexo, raca, dataNasc):
        self.nome = nome
        self.cpf = cpf
        self.sexo = sexo
        self.raca = raca
        self.dataNasc = dataNasc


# class Comorbidade(Base, SerializerMixin):
#     __tablename__ = 'comorbidades'

#     idComorbidades = Column(Integer, primary_key=True)
#     Descricao = Column(String(150, 'utf8_bin'), nullable=False)

# ==================================================
# Tabelas adicionadas para a tela de adm




class TemposContatoAcompanhamento(Base, SerializerMixin):
    __tablename__ = 'tempos_contato_acompanhamento'

    id = Column(Integer, primary_key=True)
    intervalo_contato = Column('intervalo_contato', Integer)
    tempo_maximo_acompanhamento = Column('tempo_maximo_acompanhamento', Integer)

    def __init__(self, intervalo_contato, tempo_maximo_acompanhamento):
        self.intervalo_contato = intervalo_contato
        self.tempo_maximo_acompanhamento = tempo_maximo_acompanhamento


# =================================================

# =================================================
# ====== TABELAS DE AGENDAMENTO/ATENDIMENTO =======
# =================================================

class Agendamento(Base, SerializerMixin):
    __tablename__ = 'agendamento'

    dia = Column('dia', DateTime)
    idProfissional = Column('idProfissional', Integer, ForeignKey(AdmSaude.id))
    idAtendimento = Column('idAtendimento', Integer, ForeignKey('atendimento.idAtendimento'))
    idUsuario = Column('idUsuario', Integer, ForeignKey(Paciente.id))
    id = Column('idAgendamento', Integer, primary_key=True)


class Atendimento(Base, SerializerMixin):
    __tablename__ = 'atendimento'

    primeiro = Column('primeiro', Boolean)
    dia = Column('dia', DateTime)
    id = Column('idAtendimento', Integer, primary_key=True)
    idInicial = Column('idInicial', Integer, ForeignKey('atendimento_inicial.id'))

    # -------Domicilio-------
    moraSozinho = Column('moraSozinho', Boolean)
    qntPessoasMesmoDomicilio = Column('qntPessoasMesmoDomicilio', Integer)
    # qualRelacao = Column('qualRelacao', Enum(Parentesco)) #Deveria condicionar a quantidade ao item anterior?
    # familiarDoencaCronica = Column('familiarDoencaCronica', Boolean) #nao se aplica como null?
    # quaisDoencasCronicas = Column('quaisDoencasCronicas', Enum(DoencasCronicas))
    # mulherGravida = Column('mulherGravida', Boolean)
    # nomeMulheresGravidas = Column('nomeMulheresGravidas', String)

    # -------Visitas-------
    recebeuVisita = Column('recebeuVisita', Boolean)  # Nao opinou como null?
    quemFoiAVisita = Column('quemFoiAVisita', String)
    porqueRecebeuVisita = Column('porqueRecebeuVisita', String)

    # Isolamento Domiciliar
    consegueIsolamentoDomiciliar = Column('consegueIsolamentoDomiciliar', Boolean)
    porqueMantemIsolamento = Column('porqueMantemIsolamento', String)
    porqueNaoMantemIsolamento = Column('porqueNaoMantemIsolamento', String)

    consegueManterQuarentena = Column('consegueManterQuarentena', Boolean)
    quantosDias = Column('quantosDias', Integer)  # Se sim

    # motivosSairDeCasaField = Column('motivosSairDeCasaField', Enum(MotivosSair)) #Se nao. Adicionar campo para "Outros"?

    estrategiaCompraAlimentoField = Column('estrategiaCompraAlimentoField', String)  # ???
    cuidadoPessoaSairCasa = Column('cuidadoPessoaSairCasa', String)  # ???

    # -------Perguntas sobre os sintomas da Covid-19-------
    # sintomaCovid19Field = Column('sintomaCovid19Field', Enum(Sintomas)) #Tem um Enum mas o campo é um select...
    apresentouFebreQuantosGraus = Column('apresentouFebreQuantosGraus', Float)

    tomouAlgumMedicamentoProsSintomas = Column('tomouAlgumMedicamentoProsSintomas', Boolean)
    # qualMedicamentoTomou = Column('qualMedicamentoTomou', String)#Se sim
    # quemIndicouMedicamento = Column('quemIndicouMedicamento', Enum(IndicadorMedicamento))
    # quemIndicouField = Column('quemIndicouField', String) #Para "outros"
    # comoTomaMedicamento = Column('comoTomaMedicamento', String)

    # alguemMaisApresentaSintomaEmCasa = Column('alguemMaisApresentaSintomaEmCasa', Boolean)
    # quemApresentouSintomas = Column('quemApresentouSintomas', String)
    # quaisSintomasApresentou = Column('quaisSintomasApresentou', Enum(SintomasFamiliar))
    # seFebreDeQuanto = Column('seFebreDeQuanto', Float)

    # -------Encerramento-------
    # outroAtendimentoField = Column('outroAtendimentoField', Enum(OrientacaoFinal))
    anotarOrientacoes = Column('anotarOrientacoes', String)


class AtendimentoInicial(Base, SerializerMixin):
    __tablename__ = 'atendimento_inicial'

    id = Column('id', Integer, primary_key=True)

    # -------Dados pessoais-------
    endereco = Column('endereco', String)

    # -------Comorbidades------- (Tirar isso depois)
    # comorbidades = Column('comorbidades', String)
    # dataPrimeiroSintoma = Column('dataPrimeiroSintoma', DateTime)

    # -------Doenças crônicas-------
    doencaCronica = Column('doencaCronica', Boolean)  # Precisa desse boolean? Se não, apenas não terá nenhum registro
    # listaDoencasPaciente = Column('listaDoencasPaciente', Enum(DoencasCronicas)) #Retirar

    # ------Medicamentos-------
    checkRemedioPaciente = Column('checkRemedioPaciente', Boolean)  # precisa disso? Se não, não haverá nenhum registro.
    # listaMedicamentosPaciente = Column('listaMedicamentosPaciente', String) #Vai virar tabela Medicamento
    # doseRemedioPaciente = Column('doseRemedioPaciente', String) #Vai estar na tabela Medicamento
    # tmpRemedioPaciente = Column('tmpRemedioPaciente', String) #Vai estar na tabela Medicamento
    # indicouRemedioPaciente = Column('indicouRemedioPaciente', Boolean) #Vai estar na tabela Medicamento
    # quemIndicouRemedioPaciente = Column('quemIndicouRemedioPaciente', Enum(IndicadorMedicamento)) #Vai estar na tabela Medicamento

    # -------Estratégias de Saúde Familiar-------
    esf = Column('esf',
                 Integer)  # Foreign Key, existe uma tabela de esf. Se a pessoa responder não, apenas deixar esse valor null.

    # -------Características do domicílio e auxílios governamentais-------
    qntComodos = Column('qntComodos', Integer)
    aguaEncanada = Column('aguaEncanada', Boolean)

    recebeAuxilio = Column('recebeAuxilio', Boolean)  # Indicar "pediu e não recebeu" como null?
    # Podemos indicar o "pediu e não recebeu" como true aqui e
    # se ele tiver algum auxilio, basta verificar registro na tabela
    # quaisAuxilios = Column('quaisAuxilios', Enum(BeneficiosSociais)) #Vai sair

# Problemas: Alguns campos com Enums são selects
