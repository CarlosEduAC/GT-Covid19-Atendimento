from .inputs import *
informacoesBasicas = {
    "name": "Informações Básicas do Paciente",
    "inputs": [
        nome,
        cpf,
        telefone,
        aniversario,
        comorbidades,
        dataPrimeiroSintoma,
    ]
}

doencasCronicas = {
    "name": "Doenças Crônicas",
    "inputs": [
        doencaCronica,
    ]
}

medicamentos = {
    "name": "Medicamentos",
    "inputs": [
        checkRemedioPaciente
    ]
}

esfReferencia = {
    "name": "ESF de Referência",
    "inputs": [
        esf
    ]
}
