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
        sexo,
        raca
    ]
}

condicaoclinica = {
    "name": "Comorbidades",
    "inputs": [
        comorbidades,
        dataPrimeiroSintoma,
    ]
}

domicilio = {
    "name": "Domicílio",
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

visitas = {
    "name": "Visitas",
    "inputs": [
        recebeuVisita,
    ]
}

sintomascovid = {
    "name": "Perguntas sobre os sintomas da Covid-19",
    "inputs": [
        apresentouSintomasCovid19,
        apresentouFebreQuantosGraus,
        tomouAlgumMedicamentoProsSintomas,
        quemIndicouMedicamento,
        qualMedicamentoTomou,
        comoTomaMedicamento,
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
