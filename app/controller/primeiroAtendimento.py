from dao.paciente import Paciente
from datetime import datetime


def registrar(form):
    pass


# ======================================
# ============== Paciente ==============
# ======================================


# # Outros
# comorbidades = form['comorbidades']
# dataPrimeiroSintoma = datetime.strptime(form['dataPrimeiroSintoma'], '%d/%m/%Y').date()
# doencaCronica = form['doencaCronica']
# listaDoencasPaciente = form['listaDoencasPaciente']
# checkRemedioPaciente = form['checkRemedioPaciente']
# listaMedentoicamentosPaciente = form['listaMedicamentosPaciente']
# doseRemedioPaciente = form['doseRemedioPaciente']
# tmpRemedioPaciente = form['tmpRemedioPaciente']
# indicouRemedioPaciente = form['indicouRemedioPaciente']
# couRquemIndicouRemedioPaciente = form['quemIndicouRemedioPaciente']
# Estratégia_de_Saude_da_Família = form['esf']
# Estratégia_de_Saude_da_Família_Descricao = form['esfDescricao']
#
# # Manipulando Paciente
# Paciente().savePaciente(nome, cpf, sexo, raca, aniversario)
# Paciente().selectPaciente()


def paciente(form) -> Paciente:
    nome = form['nome']
    cpf = form['cpf']
    telefone = form['telefone']
    endereco = form['endereco']
    data_nasc = datetime.strptime(form['data_nasc'], '%d/%m/%Y').date() if len(form['data_nasc']) != 0 else None
    id_etnia = form['id_etnia']
    id_genero = form['id_genero']

    return Paciente(
        nome=nome,
        cpf=cpf,
        telefone=telefone,
        endereco=endereco,
        data_nasc=data_nasc,
        id_etnia=id_etnia,
        id_genero=id_genero
    )
