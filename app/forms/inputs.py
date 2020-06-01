nome = {
    "name": "nome",
    "label": "Qual o seu nome?",
    "placeholder": "Nome do paciente",
    "required": True
}

cpf = {
    "name": "cpf",
    "label": "Qual o seu CPF?",
    "placeholder": "123456789-00",
    "required": True
}

telefone = {
    "name": "telefone",
    "label": "Qual o seu número de telefone?",
    "placeholder": "(12) 3456-7890"
}

aniversario = {
    "name": "aniversario",
    "label": "Qual a data do seu aniversário?",
}

comorbidades = {
    "name": "comorbidades",
    "label": "Quais as suas comorbidades?",
}

dataPrimeiroSintoma = {
    "name": "dataPrimeiroSintoma",
    "label": "Qual a data do surgimento dos primeiros sintomas?"
}

doencaCronica = {
    "type": "radio",
    "name": "doencaCronica",
    "label": "O Sr/Srª apresenta alguma doença crônica?",
    "options": ["Sim", "Não", "Não opinou"],
    "fields": [
        {
            "name": "listaDoencasPaciente",
            "label": "Caso sim, qual(is)?",
            "class": "tagsinput"
        }
    ]
}

listaMedicamentosPaciente = {
    "name": "listaMedicamentosPaciente",
    "label": "Caso sim, qual(is)?",
    "class": "tagsinput"
}

doseRemedioPaciente = {
    "name": "doseRemedioPaciente",
    "label": "Como toma esse medicamento?",
    "placeholder": "Dose, quantidade de vezes ao dia",
    "required": True
}

tmpRemedioPaciente = {
    "name": "tmpRemedioPaciente",
    "label": "Há quanto tempo toma esses medicamentos?",
    "placeholder": "123 dias"
}

quemIndicouRemedioPaciente = {
    "type": "radio",
    "name": "quemIndicouRemedioPaciente",
    "label": "Caso sim, quem?",
    "required": True,
    "options": [
        "Médico",
        "Enfermeiro",
        "Vizinho/Familiar/Amigo/Conhecido",
        "Dentista",
        "Outros"
    ]
}

indicouRemedioPaciente = {
    "type": "radio",
    "name": "indicouRemedioPaciente",
    "label": "Alguém indicou o uso desses medicamentos?",
    "required": True,
    "options": ["Sim", "Não", "Não opinou"],
    "fields": [
        quemIndicouRemedioPaciente
    ]
}

checkRemedioPaciente = {
    "type": "radio",
    "name": "checkRemedioPaciente",
    "label": "O Sr/Srª toma algum medicamento diariamente?",
    "required": True,
    "options": ["Sim", "Não", "Não opinou"],
    "fields": [
        listaMedicamentosPaciente,
        doseRemedioPaciente,
        tmpRemedioPaciente,
        indicouRemedioPaciente
    ]
}

esf = {
    "type": "radio",
    "name": "esf",
    "label": "O Sr/Srª é acompanhado por alguma Estratégia de Saúde da Família?",
    "required": True,
    "options": [
        "Sim",
        "Não",
        "Não opinou"
    ],
    "fields": [
        {
            "name": "esfDescricao",
            "label": "Se sim, qual?",
            "placeholder": "Estratégia de Saúde da Família - ESF"
        }
    ]
}
