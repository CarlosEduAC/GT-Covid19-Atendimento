from controller.database import Database
from models.models import AdmSaude, Paciente, Cidade
from models.modelsDomainTable import Etnia, Genero
from werkzeug.security import generate_password_hash
from models.models import TempoContatoAcompanhamento
from models.modelsDomainTable import EstrategiaSaudeFamiliar

def getUsers(id_cidade=None):
    try:
        db = Database()

        if(id_cidade is not None):
            return db.selectAllDataByFilter(AdmSaude, id_cidade = id_cidade)

        return db.selectAllData(AdmSaude)
    except:
        return [] 

def removeUser(id):
    db = Database()
    db.delete(AdmSaude, id)

def genero_etnia():
    db = Database()
    genero = db.selectAllData(Genero)
    etnia = db.selectAllData(Etnia)
    return genero, etnia

def get_cidades():
    db = Database()
    return db.selectAllData(Cidade)

def updateUser(id, name, crm, cpf, supervisor, senha=None, id_cidade=None):

    db = Database()
    
    adm = None
    if senha is None:
        adm = AdmSaude(name, crm, cpf, supervisor, id_cidade = id_cidade)
    
    else:
        adm = AdmSaude(name, crm, cpf, supervisor, senha, id_cidade)
    
    adm.id = id
    db.updateData(AdmSaude, adm, id)


# A princípio, a tabela TempoContatoAcompanhamento
# sempre terá apenas uma entrada. Situaçao provisória.
def getTimes(id_cidade=None):
    db = Database()
    
    if(id_cidade is not None):
        times = db.selectAllDataByFilter(TempoContatoAcompanhamento, id_cidade = id_cidade)
    else:
        times = db.selectAllData(TempoContatoAcompanhamento)
    
    if len(times) == 0:
        return 48, 16
    times = times[0]
    return times["intervalo_contato"], times["tempo_maximo_acompanhamento"]

def updateTimes(intervalo, maximo, id_cidade=None):
    db = Database()
    times = db.selectAllDataByFilter(TempoContatoAcompanhamento, id_cidade=id_cidade)
    if len(times) == 0:
        db.saveData(TempoContatoAcompanhamento(intervalo, maximo, id_cidade))
    else:
        id = times[0]['id']
        tempo = TempoContatoAcompanhamento(intervalo, maximo, id_cidade)
        tempo.id = id
        db.updateData(TempoContatoAcompanhamento, tempo, id)

#==================================================

def getEsf(id_cidade=None):
    db = Database()

    if id_cidade is not None:
        return db.selectAllDataByFilter(EstrategiaSaudeFamiliar, id_cidade = id_cidade)

    return db.selectAllData(EstrategiaSaudeFamiliar)
    
def newEsf(name, id_cidade):

    esf = EstrategiaSaudeFamiliar(name, id_cidade)

    db = Database()
    db.saveData(esf)

def deleteEsf(id):
    db = Database()
    db.delete(EstrategiaSaudeFamiliar, id)