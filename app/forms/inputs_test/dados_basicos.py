from controller.database import Database
from models.modelsDomainTable import Sexo, Raca

db = Database()

nome = {
    "name": "nome",
    "label": "Nome completo",
    "placeholder": "Nome do paciente",
    "required": True
}

cpf = {
    "name": "cpf",
    "label": "CPF",
    "required": True,
    "mask": "999.999.999-99"
}

telefone = {
    "name": "telefone",
    "label": "Telefone",
    "mask": "(99) 99999999?9",
    "placeholder": "(99) 999999999"
}

nascimento = {
    "type": "date",
    "name": "nascimento",
    "label": "Data de nascimento",
}

sexo = {
    "type": "select",
    "name": "sexo",
    "label": "Sexo",
    "required": True,
    "options": db.selectAllData(Sexo)
}

raca = {
    "type": "select",
    "name": "raca",
    "label": "Raça",
    "required": True,
    "options": db.selectAllData(Raca)
}

endereco = {
    "name": "endereco",
    "label": "Endereço",
}
