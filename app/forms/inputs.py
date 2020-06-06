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

sexo = {
    "type": "radio",
    "name": "sexo",
    "label": "Qual o seu sexo? ",
    "required": True,
    "options": [
        "Masculino",
        "Feminino",
        "Não opinou"
    ]
}

doencaCronica = {
    "type": "radio",
    "name": "doencaCronica",
    "label": "O Sr/Srª apresenta alguma doença crônica?",
    "options": [
        {
            "label": "Sim",
            "fields": [
                {
                    "name": "listaDoencasPaciente",
                    "label": "Caso sim, qual(is)?",
                    "class": "tagsinput"
                }
            ]
        },
        {
            "label": "Não"
        },
        {
            "label": "Não opinou"
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
    "required": True,
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
        {
            "label": "Médico"
        },
        {
            "label": "Enfermeiro"
        },
        {
            "label": "Vizinho/Familiar/Amigo/Conhecido"
        },
        {
            "label": "Dentista"
        },
        {
            "label": "Outros"
        }
    ]
}

indicouRemedioPaciente = {
    "type": "radio",
    "name": "indicouRemedioPaciente",
    "label": "Alguém indicou o uso desses medicamentos?",
    "required": True,
    "options": [
        {
            "label": "Sim",
            "fields": [
                quemIndicouRemedioPaciente
            ]
        },
        {
            "label": "Não"
        },
        {
            "label": "Não opinou"
        }
    ]
}

checkRemedioPaciente = {
    "type": "radio",
    "name": "checkRemedioPaciente",
    "label": "O Sr/Srª toma algum medicamento diariamente?",
    "required": True,
    "options": [
        {
            "label": "Sim",
            "fields": [
                listaMedicamentosPaciente,
                doseRemedioPaciente,
                tmpRemedioPaciente,
                indicouRemedioPaciente
            ]
        },
        {
            "label": "Não"
        },
        {
            "label": "Não opinou"
        }
    ]
}

esf = {
    "type": "radio",
    "name": "esf",
    "label": "O Sr/Srª é acompanhado por alguma Estratégia de Saúde da Família?",
    "required": True,
    "options": [
        {
            "label": "Sim",
            "fields": [
                {
                    "name": "esfDescricao",
                    "label": "Se sim, qual?",
                    "placeholder": "Estratégia de Saúde da Família - ESF"
                }
            ]
        },
        {
            "label": "Não"
        },
        {
            "label": "Não opinou"
        }
    ]    
}

# Domicilio

endereco = {
    "name": "endereco",
    "label": "Para começar, o Sr/Srª poderia me confirmar seu endereço, por favor? (Caso haja divergências da ficha, anotar abaixo)",
}

moraSozinho = {
    "name": "moraSozinho",
    "type": "radio",
    "label": "O Sr/Srª mora sozinho?",
    "required": True,
    "options": [
        {
            "label": "Sim"
        },
        {
            "label": "Não",
            "fields": [
                {
                    "name": "qntPessoasMesmoDomicilio",
                    "label": "Quantas pessoas moram com você?"
                },
                {
                    "name": "qntPessoasMesmoDomicilio",
                    "label": "Qual a sua relação (pai, filho, tio, etc) com cada pessoa que mora com você e idade de cada uma delas?"
                },
                {
                    "type": "radio",
                    "name": "familiarDoencaCronica",
                    "label": "Alguma delas apresenta alguma doença crônica?",
                    "required": True,
                    "options": [
                        {
                            "label": "Sim",
                            "fields": [
                                {
                                    "name": "quaisDoencasCronicas",
                                    "label": "Caso sim, quem e qual(is) doença crônica apresenta?"
                                }
                            ]
                        },
                        {
                            "label": "Não"
                        },
                        {
                            "label": "Não se aplica, mora sozinho"
                        }
                    ]
                },
                {
                    "type": "radio",
                    "name": "mulherGravida",
                    "label": "Caso haja mulheres no domicílio: algumas delas está grávida?",
                    "required": True,
                    "options": ["Sim", "Não", ""],
                    "options": [
                        {
                            "label": "Sim",
                            "fields": [
                                {
                                    "name": "nomeMulheresGravidas",
                                    "label": "Se sim, quem?"
                                }
                            ]
                        },
                        {
                            "label": "Não"
                        },
                        {
                            "label": "Não se aplica, não há mulheres no domicílio"
                        }
                    ]
                },
            ]
        }
    ]
}

# Características do domicílio e auxílios governamentais

qntComodos = {
    "name": "qntComodos",
    "label": "Quantos cômodos tem a sua casa?",
    "required": True,
}

aguaEncanada = {
    "name": "aguaEncanada",
    "type": "radio",
    "label": "O Sr/Sr tem acesso a agua na torneira de casa?",
    "required": True,
    "options": [
        {
            "label": "Sim"
        },
        {
            "label": "Não"
        }
    ],
}

recebeAuxilio = {
    "name": "recebeAuxilio",
    "type": "radio",
    "label": "O Sr/Srª está recebendo algum auxílio do governo durante esse período da pandemia?",
    "required": True,
    "options": [
        {
            "label": "Sim",
            "fields": [
                {
                    "name": "quaisAuxilios",
                    "label": "Quais?",
                }
            ]
        },
        {
            "label": "Não"
        },
        {
            "label": "Já pedi mas ainda não recebi"
        }
    ]    
}

# Isolamento domiciliar

consegueIsolamentoDomiciliar = {
    "name": "consegueIsolamentoDomiciliar",
    "type": "radio",
    "label": "O Sr/Srª está conseguindo se manter isolado dos demais?",
    "hint": "Manter-se isolado significa estar sozinho em um cômodo da casa, sem acesso aos demais habitantes a esse cômodo. Se o usuário responder não, orientar o isolamento domiciliar, quando possível. Caso não seja possível o isolamento, orientar estratégias de redução de risco de transmissão.",
    "required": True,
    "options": [
        {
            "label": "Sim"
        },
        {
            "label": "Não"
        },
        {
            "label": "Não se aplica, mora sozinho"
        }
    ],
}

consegueManterQuarentena = {
    "name": "consegueManterQuarentena",
    "type": "radio",
    "label": "Você e as pessoas com quem mora estão conseguindo se manter em casa?",
    "required": True,
    "options": [
        {
            "label": "Sim",
            "fields": [
                {
                    "name": "quantosDias",
                    "label": "Há Quantos dias?",
                }
            ]
        },
        {
            "label": "Não"
        },
        {
            "label": "Sai só para atividades essenciais (banco, supermercado, etc)."
        }
    ]
}

motivosSairDeCasa = {
    "name": "motivosSairDeCasa",
    "type": "checkbox",
    "label": "Se não: quais são os motivos para sair de casa?",
    "options": [
        {

        }
    ]
}
