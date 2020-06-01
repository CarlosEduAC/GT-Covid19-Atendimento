import forms.inputs as input

informacoesBasicas = {
    "name": "Informações Básicas do Paciente",
    "inputs": [
        input.nome,
        input.cpf,
        input.telefone,
        input.aniversario,
        input.comorbidades,
        input.dataPrimeiroSintoma,
    ]
}

doencasCronicas = {
    "name": "Doenças Crônicas",
    "inputs": [
        input.doencaCronica,
    ]
}

medicamentos = {
    "name": "Medicamentos",
    "inputs": [
        input.checkRemedioPaciente
    ]
}

esfReferencia = {
    "name": "ESF de Referência",
    "inputs": [
        input.esf
    ]
}
