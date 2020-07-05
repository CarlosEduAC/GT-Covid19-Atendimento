from controller.database import Database
from models.models import Paciente
from datetime import datetime
from controller.primeiroAtendimento import data_or_null, only_num

def savePaciente (nome, cpf, telefone, dataNasc, id_etnia, id_genero, endereco):

    nome = data_or_null(nome)
    cpf = data_or_null(cpf, only_num)
    telefone = data_or_null(telefone, only_num)
    endereco = data_or_null(endereco)
    dataNasc = datetime.strptime(dataNasc, '%d/%m/%Y').date() if len(dataNasc) != 0 else None
    id_etnia = data_or_null(id_etnia, int)
    id_genero = data_or_null(id_genero, int)

    paciente = Paciente(nome, cpf, telefone, dataNasc, id_etnia, id_genero, endereco)

    try:
        db = Database()
        db.saveData(paciente)
    except Exception as e:
        print (e)

def selectPaciente ():
    pacientes = []
        
    try:
        db = Database()
        response = db.selectAllData(Paciente)
        for paciente in response:
            pacientes.append(paciente)
    except Exception as e:
        print(e)

    print(pacientes)

def getPacientes():
    try:
        db = Database()

        return db.selectAllData(Paciente)
    except:
        return [] 

def removePaciente(id):
    db = Database()
    db.delete(Paciente, id)


def updatePaciente(id, nome, cpf, telefone, dataNasc, id_etnia, id_genero, endereco):

    db = Database()

    paciente = Paciente(nome,cpf,telefone,dataNasc,id_etnia,id_genero,endereco)
    paciente.id = id

    db.updateData(Paciente, paciente, id)

