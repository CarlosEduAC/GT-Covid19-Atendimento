from .inputs import *

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

domicilio = {
    "name": "Domicilio",
    "inputs": [
        endereco,
        moraSozinho
    ]
}

caracteristicasDomicilioAuxilio = {
    "name": "Características do domicílio e auxílios governamentais",
    "inputs": [
        qntComodos,
        aguaEncanada,
        recebeAuxilio
    ]
}

isolamentoDomiciliar = {
    "name": "Isolamento Domiciliar",
    "inputs": [
        consegueIsolamentoDomiciliar,
        consegueManterQuarentena,
        motivosSairDeCasa
    ]
}
