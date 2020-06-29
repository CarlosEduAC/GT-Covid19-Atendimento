from .inputs import *
from forms.inputs_test.dados_basicos import *

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
        mantem_quarentena
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
    "inputs": [
        apresentouSintomasCovid19,
        apresentouFebreQuantosGraus,
        tomouAlgumMedicamentoProsSintomas,
        alguemMaisApresentaSintomaEmCasa
    ]
}

orientacoesfinais = {
    "name": "Encerramento do atendimento/Orientações finais",
    "inputs": [
        orientacaoFinal,
        anotarOrientacoes
    ]
}
