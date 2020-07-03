from controller.database import Database
from models.models import AdmSaude, Paciente
from werkzeug.security import generate_password_hash
from models.models import TempoContatoAcompanhamento
from models.modelsDomainTable import EstrategiaSaudeFamiliar

def getUsers():
    try:
        db = Database()

        return db.selectAllData(AdmSaude)
    except:
        return [] 

def removeUser(id):
    db = Database()
    db.delete(AdmSaude, id)


def updateUser(id, name, crm, cpf, supervisor, senha=None):

    db = Database()
    print("Supervisor {}".format(supervisor))
    #new_adm = AdmSaude(id, name, crm, cpf, supervisor, "")

    print(crm)

    if senha is None:
        db.updateData(AdmSaude, AdmSaude(name, crm, cpf, supervisor), id)
    
    else:
        db.updateData(AdmSaude, AdmSaude(name, crm, cpf, supervisor, senha), id)

# A princípio, a tabela TempoContatoAcompanhamento
# sempre terá apenas uma entrada. Situaçao provisória.
def getTimes():
    db = Database()
    times = db.selectAllData(TempoContatoAcompanhamento)
    if len(times) == 0:
        return 48, 16
    times = times[0]
    return times["intervalo_contato"], times["tempo_maximo_acompanhamento"]

def updateTimes(intervalo, maximo):
    db = Database()
    times = db.selectAllData(TempoContatoAcompanhamento)
    if len(times) == 0:
        db.saveData(TempoContatoAcompanhamento(intervalo, maximo))
    else:
        id = times[0]['id']
        db.updateData(TempoContatoAcompanhamento, TempoContatoAcompanhamento(intervalo, maximo), id)

#==================================================

def getEsf():
    db = Database()
    return db.selectAllData(EstrategiaSaudeFamiliar)
    
def newEsf(name):

    esf = EstrategiaSaudeFamiliar(name)

    db = Database()
    db.saveData(esf)