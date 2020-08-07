from controller.database import Database
from models.models import Paciente
from datetime import datetime
from controller.formfuncs import *


def inserirPaciente(nome, cpf, telefone, endereco, data_nasc, id_etnia, id_genero):
    db = Database()
    paciente = db.selectIf(Paciente, cpf=cpf)
    if paciente:
        # atualizar paciente
        updatePaciente(paciente.id, nome, cpf, telefone, id_etnia, id_genero, data_nasc, endereco)
        return paciente.id
    else:
        new_paciente = Paciente(nome, cpf, telefone, data_nasc, id_etnia, id_genero, endereco)
        db.saveData(new_paciente)
        return db.selectIf(Paciente, cpf=cpf).id


def savePaciente(nome, cpf, telefone, dataNasc, id_etnia, id_genero, endereco):
    nome = data_or_null(nome)
    cpf = data_or_null(cpf, only_num)
    telefone = data_or_null(telefone, only_num)
    endereco = data_or_null(endereco)
    id_etnia = data_or_null(id_etnia, int)
    id_genero = data_or_null(id_genero, int)

    paciente = Paciente(nome, cpf, telefone, dataNasc, id_etnia, id_genero, endereco)

    try:
        db = Database()
        db.saveData(paciente)
    except Exception as e:
        print(e)


def selectPaciente():
    pacientes = []

    try:
        db = Database()
        response = db.selectAllData(Paciente)
        for paciente in response:
            pacientes.append(paciente)
    except Exception as e:
        print(e)

    print(pacientes)


def getPaciente(id):
    db = Database()

    return db.selectIf(Paciente, id=id)


def getPacientes():
    try:
        db = Database()

        return db.selectAllData(Paciente)
    except:
        return []


def removePaciente(id):
    db = Database()
    db.delete(Paciente, id)


def updatePaciente(id, nome, cpf, telefone, id_etnia, id_genero, dataNasc, endereco):
    db = Database()

    paciente = Paciente(nome, cpf, telefone,
                        dataNasc,
                        id_etnia, id_genero, endereco)
    paciente.id = id

    db.updateData(Paciente, paciente, id)
