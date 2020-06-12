from controller.database import Database
from models.models import AdmSaude, Usuario

def getUsers():
    try:
        db = Database()
        return db.selectAllData(Usuario)
    except:
        return [] 

def getAdms():
    try:
        db = Database()
        return db.selectAllData(AdmSaude)
    except:
        return [] 

def removeUser(id):

    db = Database()
    db.delete(Usuario, id)

def removeAdm(id):

    db = Database()
    db.delete(AdmSaude, id)

def updateUser(id, name, cpf, crm):

    db = Database()
    session = db.Session()
    session.query(Usuario).filter(Usuario.id == id).update(
        { Usuario.name : name,
          Usuario.cpf : cpf,
          Usuario.crm : crm })
    session.commit()

def updateAdm(id, nome, crm, supervisor):

    db = Database()
    session = db.Session()
    session.query(AdmSaude).filter(AdmSaude.idadm_saude == id).update(
        {AdmSaude.nome : nome,
        AdmSaude.CRM : crm,
        AdmSaude.supervisor : supervisor})
    session.commit()
