from controller.database import Database
from models.modelsGenerated import *


def registrar(formulario):

    nome = formulario.form['nome']
    cpf = formulario.form['cpf']
    telefone = formulario.form['telefone']
    aniversario = formulario.form['aniversario']
    comorbidades = formulario.form['comorbidades']
    dataPrimeiroSintoma = formulario.form['dataPrimeiroSintoma']
    doencaCronica = formulario.form['doencaCronica']
    listaDoencasPaciente = formulario.form['listaDoencasPaciente']
    checkRemedioPaciente = formulario.form['checkRemedioPaciente']
    listaMedentoicamentosPaciente = formulario.form['listaMedentoicamentosPaciente']
    doseRemedioPaciente = formulario.form['doseRemedioPaciente']
    tmpRemedioPaciente = formulario.form['tmpRemedioPaciente']
    indicouRemedioPaciente = formulario.form['indicouRemedioPaciente']
    couRquemIndicouRemedioPaciente = formulario.form['couRquemIndicouRemedioPaciente']
    Estratégia_de_Saúde_da_Família = formulario.form['esf']
    Estratégia_de_Saúde_da_Família_Descricao = formulario.form['esfDescricao']

    print(nome , Estratégia_de_Saúde_da_Família_Descricao)

    #paciente = Paciente(nome, cpf, ocupacao, sexo, raca,
                        #datetime.strptime(dataNasc, '%d/%m/%Y'))

    #db = Database()
    #db.saveData(paciente)

    #return render_template('paciente.html')
