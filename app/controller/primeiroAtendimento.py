from controller.util import savePaciente, selectPaciente
from datetime import datetime

def registrar(formulario):
    # Paciente
    nome = formulario['nome']
    cpf = formulario['cpf']
    telefone = formulario['telefone']
    sexo = formulario['sexo']
    raca = 'Não opinou' #formulario['raca']
    aniversario = datetime.strptime(formulario['aniversario'], '%d/%m/%Y').date()
    # Outros
    comorbidades = formulario['comorbidades']
    dataPrimeiroSintoma = datetime.strptime(formulario['dataPrimeiroSintoma'], '%d/%m/%Y').date()
    doencaCronica = formulario['doencaCronica']
    listaDoencasPaciente = formulario['listaDoencasPaciente']
    checkRemedioPaciente = formulario['checkRemedioPaciente']
    listaMedentoicamentosPaciente = formulario['listaMedicamentosPaciente']
    doseRemedioPaciente = formulario['doseRemedioPaciente']
    tmpRemedioPaciente = formulario['tmpRemedioPaciente']
    indicouRemedioPaciente = formulario['indicouRemedioPaciente']
    couRquemIndicouRemedioPaciente = formulario['quemIndicouRemedioPaciente']
    Estratégia_de_Saude_da_Família = formulario['esf']
    Estratégia_de_Saude_da_Família_Descricao = formulario['esfDescricao']
    
    # Manipulando Paciente
    savePaciente (nome, cpf, sexo, raca, aniversario)
    selectPaciente ()