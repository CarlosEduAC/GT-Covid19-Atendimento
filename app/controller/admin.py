# from controller.database import Database
# from models.models import AdmSaude

# # def getUsers():
# #     try:
# #         db = Database()
# #         session = db.Session()

# #         return session.query(AdmSaude, Usuario).filter(AdmSaude.idadm_saude == Usuario.id).all()
# #     except:
# #         return [] 


# def removeUser(id):

#     db = Database()
#     db.delete(AdmSaude, id)
#     # db.delete(Usuario, id)


# # def updateUser(id, name, crm, cpf, supervisor):

# #     db = Database()
# #     session = db.Session()
# #     session.query(AdmSaude).filter(AdmSaude.idadm_saude == id).update(
# #         { AdmSaude.nome : name,
# #           AdmSaude.CRM : crm,
# #           AdmSaude.supervisor : supervisor })
# #     session.query(Usuario).filter(Usuario.id == id).update(
# #         { Usuario.cpf : cpf}
# #     )
# #     session.commit()

