from .inputs import *
from forms.inputs_test.dados_basicos import *

tentativa = {
    "name": "Tentativa",
    "inputs": [
        select_realizar_tentativa
    ]
}

doencasCronicas = {
    "name": "Doenças Crônicas",
    "inputs": [
        select_doenca_cronica
    ]
}

medicamentos = {
    "name": "Medicamentos",
    "inputs": [
        toma_medicamento_diariamente
    ]
}

esfReferencia = {
    "name": "ESF de Referência",
    "inputs": [
        select_estrategia_saude_familia
    ]
}

informacoesBasicas = {
    "name": "Informações Básicas do Paciente",
    "inputs": [
        [nome, cpf, telefone],
        [nascimento, sexo, raca],
        [endereco, None]
    ]
}

domicilio = {
    "name": "Domicílio",
    "inputs": [
        select_mora_sozinho
    ]
}

caracteristicasDomicilioAuxilio = {
    "name": "Características do domicílio e auxílios governamentais",
    "inputs": [
        qnt_comodos,
        select_agua_encanada,
        select_auxilios
    ]
}

isolamentoDomiciliar = {
    "name": "Isolamento Domiciliar",
    "inputs": [
        select_isolamento_domiciliar,
        consegueManterQuarentena
    ]
}

visitas = {
    "name": "Visitas",
    "inputs": [
        select_recebeu_visitas,
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
