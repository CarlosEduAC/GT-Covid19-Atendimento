from controller.database import Database
from models.models import Paciente

class Paciente:
    def savePaciente (self, nome, cpf, sexo, raca, dataNasc):
        paciente = Paciente(sexo=sexo, raca=raca, dataNasc=dataNasc) #nome=nome, cpf=cpf, 

        try:
            db = Database()
            db.saveData(paciente)
        except Exception as e:
            print (e)

    def selectPaciente (self):
        pacientes = []
        
        try:
            db = Database()
            response = db.selectAllData(Paciente)
            for paciente in response:
                pacientes.append(paciente)
        except Exception as e:
            print(e)

        print(pacientes)