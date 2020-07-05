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
    
    adm = None
    if senha is None:
        adm = AdmSaude(name, crm, cpf, supervisor)
    
    else:
        adm = AdmSaude(name, crm, cpf, supervisor, senha)
    
    adm.id = id
    db.updateData(AdmSaude, adm, id)


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
        tempo = TempoContatoAcompanhamento(intervalo, maximo)
        tempo.id = id
        db.updateData(TempoContatoAcompanhamento, tempo, id)

#==================================================

def getEsf():
    db = Database()
    return db.selectAllData(EstrategiaSaudeFamiliar)
    
def newEsf(name):

    esf = EstrategiaSaudeFamiliar(name)

    db = Database()
    db.saveData(esf)