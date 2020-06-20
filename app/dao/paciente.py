from controller.database import Database
from models.models import Paciente

def savePaciente (nome, cpf, sexo, raca, dataNasc):
    paciente = Paciente(nome, cpf, sexo, raca, dataNasc)

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


def updatePaciente(id, nome, cpf, sexo, raca, dataNasc):

    db = Database()

    #new_adm = AdmSaude(id, name, crm, cpf, supervisor, "")

    db.updateData(Paciente, {'nome' : nome,
                             'cpf' : cpf,
                             'sexo' : sexo,
                             'raca' : raca,
                             'dataNasc' : dataNasc}, id)