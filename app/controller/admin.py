from controller.database import Database
from models.models import AdmSaude, TemposContatoAcompanhamento, EstrategiaSaudeFamiliar, Paciente

def getUsers():
    try:
        db = Database()

        return db.selectAllData(AdmSaude)
    except:
        return [] 

def removeUser(id):
    db = Database()
    db.delete(AdmSaude, id)


def updateUser(id, name, crm, cpf, supervisor):

    db = Database()

    #new_adm = AdmSaude(id, name, crm, cpf, supervisor, "")

    db.updateData(AdmSaude, {'name' : name,
                             'crm' : crm,
                             'cpf' : cpf,
                             'supervisor' : supervisor}, id)


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



# A princípio, a tabela TemposContatoAcompanhamento
# sempre terá apenas uma entrada. Situaçao provisória.
def getTimes():
    db = Database()
    times = db.selectAllData(TemposContatoAcompanhamento)
    if len(times) == 0:
        return 48, 16
    times = times[0]
    return times["intervalo_contato"], times["tempo_maximo_acompanhamento"]

def updateTimes(intervalo, maximo):
    db = Database()
    id = db.selectAllData(TemposContatoAcompanhamento)[0]['id']
    
    db.updateData(TemposContatoAcompanhamento, TemposContatoAcompanhamento(intervalo, maximo), id)

#==================================================

def getEsf():
    db = Database()
    return db.selectAllData(EstrategiaSaudeFamiliar)

def newEsf(name):

    esf = EstrategiaSaudeFamiliar(name)

    db = Database()
    db.saveData(esf)