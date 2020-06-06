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
        # {
        #     "type": "select",
        #     "name": "nomezinho",
        #     "label": "Label",
        #     "options": [
        #         {
        #             "label": "Campinho 1",
        #             "value": "value1",
        #         },{
        #             "label": "Campinho 1",
        #             "value": "value1",
        #         },{
        #             "label": "Campinho 1",
        #             "value": "value1",
        #         },{
        #             "label": "Campinho 1",
        #             "value": "value1",
        #         },{
        #             "label": "Campinho 1",
        #             "value": "value1",
        #         },
        #     ]
        # }
        nome,
        cpf,
        telefone,
        aniversario,
        comorbidades,
        dataPrimeiroSintoma,
        # {
        #     "type": "checkbox",
        #     "name": "test",
        #     "label": "Se não: quais são os motivos para sair de casa?",
        #     "options": [
        #         {
        #             "label": "Ir ao supermercado ou a farmácia",
        #         },
        #         {
        #             "label": "Ir ao supermercado ou a farmácia",
        #         },
        #         {
        #             "label": "Ir ao supermercado ou a farmácia",
        #         },
        #         {
        #             "label": "Outros",
        #             "field": {
        #                 "name": "asdasda",
        #                 "placeholder": "Placeholder",
        #             },
        #         },
        #     ]
        # }
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
