from datetime import datetime
from .inputs import *

""" class Section():
    def __init__(self, name, inputs):
        self.name = name
        self.inputs = inputs
    
    def inserirInfoPaciente(self, paciente):
        self.inputs[0][0].setValue(paciente.nome)
        self.inputs[0][1].setValue(paciente.cpf)
        self.inputs[0][2].setValue(paciente.telefone)
        self.inputs[1][0].setValue(datetime.strftime(paciente.data_nasc, "%d/%m/%Y"))
        self.inputs[1][1].setValue(paciente.id_genero)
        self.inputs[1][2].setValue(paciente.id_etnia)
        self.inputs[2].setValue(paciente.endereco) """

def inserirInfoPaciente(section, paciente):
    section["inputs"][0][0].setValue(paciente.nome)
    section["inputs"][0][1].setValue(paciente.cpf)
    section["inputs"][0][2].setValue(paciente.telefone)
    section["inputs"][1][0].setValue(datetime.strftime(paciente.data_nasc, "%d/%m/%Y"))
    section["inputs"][1][1].setValue(paciente.id_genero)
    section["inputs"][1][2].setValue(paciente.id_etnia)
    section["inputs"][2].setValue(paciente.endereco)

    return section

""" informacoesBasicasPreenchidas = Section(
    name = "Informações Básicas do Paciente",
    inputs = [
        [nome, cpf, telefone],
        [data_nasc, genero, etnia],
        endereco
    ]
) """


tentativa = {
    "name": "Tentativa",
    "inputs": [
        has_atendimento
    ]
}

doencasCronicas = {
    "name": "Doenças Crônicas",
    "inputs": [
        has_doenca_cronica
    ]
}

medicamentos = {
    "name": "Medicamentos",
    "inputs": [
        has_medicamento
    ]
}

esfReferencia = {
    "name": "ESF de Referência",
    "inputs": [
        has_estrategia_saude_familiar
    ]
}

informacoesBasicas = {
    "name": "Informações Básicas do Paciente",
    "inputs": [
        [nome, cpf, telefone],
        [data_nasc, genero, etnia],
        endereco
    ]
}

domicilio = {
    "name": "Domicílio",
    "inputs": [
        mora_sozinho
    ]
}

caracteristicasDomicilioAuxilio = {
    "name": "Características do domicílio e auxílios governamentais",
    "inputs": [
        qnt_comodos,
        has_agua_encanada,
        has_auxilio
    ]
}

isolamentoDomiciliar = {
    "name": "Isolamento Domiciliar",
    "inputs": [
        has_isolamento,
        mantem_quarentena,
        cuidado_sair_casa
    ]
}

visitas = {
    "name": "Visitas",
    "inputs": [
        recebeu_visita,
    ]
}

sintomascovid = {
    "name": "Perguntas sobre os sintomas da Covid-19",
    "inputs": [has_sintoma]
}

orientacoesfinais = {
    "name": "Encerramento do atendimento/Orientações finais",
    "inputs": [
        orientacao_final,
        anotar_orientacoes
    ]
}
