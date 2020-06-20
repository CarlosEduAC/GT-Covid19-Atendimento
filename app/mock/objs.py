paciente = [
    {
        "nome": "Paciente teste 1",
        "cpf": 11111111111,
        "sexo": "masculino",
        "raca": "negra",
        "dataNasc": "20/12/1997",
        "id": 1
    },
    {
        "nome": "Paciente teste 2",
        "cpf": 22222222222,
        "sexo": "masculino",
        "raca": "negra",
        "dataNasc": "16/03/1998",
        "id": 2
    }
]

admSaude = {
    "idadm_saude": 1,
    "nome": "Amd Saude de Teste",
    "crm": 464849848,
    "supervisor": False,
    "senha": "teste"
}

comorbidades = [
    {
        "idComorbidades": 1,
        "Descricao" : "Diabetes"
    },
    {
        "idComorbidades": 2,
        "Descricao" : "Hipertensão"
    },
    {
        "idComorbidades": 3,
        "Descricao" : "Alzheimer"
    },
    {
        "idComorbidades": 4,
        "Descricao" : "AIDS"
    },
    {
        "idComorbidades": 5,
        "Descricao" : "Asma"
    }
]

esf = [
    {
        "id": 1,
        "estrategia": "estrategia de teste 1"
    },
    {
        "id": 2,
        "estrategia": "estrategia de teste 2"
    }
]

agendamento = {
    "dia": "03/06/2188",
    "idProfissional": 1,
    "idAtendimento": 1,
    "idUsuario": 1,
    "id": 1
}

atendimento = {
    "primeiro": False,
    "dia": "10/12/2018",
    "id": 1,
    "idInicial": 1,
    "moraSozinho": True,
    "qntPessoasMesmoDomicilio": 1,
    "recebeuVisita": False,
    "consegueIsolamentoDomiciliar": False,
    "porqueNaoMantemIsolamento": "Trabalhar",
    "consegueManterQuarentena": True,
    "quantosDias": 2,
    "estrategiaCompraAlimentoField": "eh",
    "cuidadoPessoaSairCasa": "nope",
    "apresentouFebreQuantosGraus": 36.5,
    "tomouAlgumMedicamentoProsSintomas": False,
    "anotarOrientacoes": "Fim"
}

atendimentoInicial = {
    "id": 1,
    "endereco": "Rua de teste",
    "donecaCronica": False,
    "checkRemedioPaciente": False,
    "esf": 1,
    "qntComodos": 8,
    "aguaEncanada": True,
    "recebeAuxilio": False
}