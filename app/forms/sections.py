from datetime import datetime
from copy import deepcopy
from .inputs import *


def inserirInfoPaciente(paciente):
    return {
        "name": "Informações Básicas do Paciente",
        "inputs": [
            [
                deepcopy(nome).setValue(paciente.nome),
                deepcopy(cpf).setValue(paciente.cpf),
                deepcopy(telefone).setValue(paciente.telefone)
            ],
            [
                deepcopy(data_nasc).setValue(
                    datetime.strftime(paciente.data_nasc, "%d/%m/%Y") if paciente.data_nasc is not None else ""),
                deepcopy(genero).setValue(paciente.id_genero),
                deepcopy(etnia).setValue(paciente.id_etnia)
            ],
            deepcopy(endereco).setValue(paciente.endereco)
        ]
    }


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
    "view": "vw_atendimentos_relacoes",
    "columns": [
        "data",
        "dosagem",
        "doenca_cronica",
        "parentesco",
        "indicador",
        "sintoma",
        "data_primeiro_sintoma"
    ],
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
    "view": "atendimentos",
    "columns": [
        "data",
        "cuidado_sair_casa",
        "consegue_isolamento",
        "como_consegue",
        "porque_nao_consegue",
        "consegue_ficar_casa",
        "quantos_dias"
    ],
    "inputs": [
        has_isolamento,
        mantem_quarentena,
        cuidado_sair_casa
    ]
}

visitas = {
    "name": "Visitas",
    "view": "vw_atendimentos_visitas",
    "columns": [
        "data",
        "quem_visitou",
        "porque_visitou"
    ],
    "inputs": [
        recebeu_visita,
    ]
}

sintomascovid = {
    "name": "Perguntas sobre os sintomas da Covid-19",
    "view": "vw_atendimentos_sintoma_pessoa",
    "columns": [
        "data",
        "dosagem",
        "indicador",
        "sintoma",
        "data_primeiro_sintoma"
    ],
    "inputs": [has_sintoma]
}

orientacoesfinais = {
    "name": "Encerramento do atendimento/Orientações finais",
    "view": "vw_atendimentos_orientacoes_finais",
    "columns": [
        "data",
        "comentario",
        "outras",
    ],
    "inputs": [
        orientacao_final,
        anotar_orientacoes
    ]
}
