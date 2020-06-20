import models.enums_copia

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
    "label": "Qual a data do seu aniversário?"
}

sexo = {
    "type": "radio",
    "name": "sexo",
    "label": "Qual seu sexo?",
    "required": True,
    "options": [
        {
            "label": "Masculino",
        },
        {
            "label": "Feminino"
        },
        {
            "label": "Não opinou"
        }
    ]
}

raca = {
    "type": "radio",
    "name": "raca",
    "label": "Qual sua raça?",
    "required": True,
    "options": [
        {
            "label": "Negra",
        },
        {
            "label": "Amarela"
        },
        {
            "label": "Branca"
        },
        {
            "label": "Parda"
        },
        {
            "label": "Indígena"
        }
    ]
}

comorbidades = {
    "name": "comorbidades",
    "label": "Quais as suas comorbidades?",
    "type": "checkbox",
    "options": [
        {
            "label": "Comorbidades 1",
        },
        {
            "label": "Comorbidades 2",
        },
        {
            "label": "Outros",
            "field": {
                "name": "comorbidadesField",
                "placeholder": "Placeholder",
            },
        },
    ]
}

dataPrimeiroSintoma = {
    "name": "dataPrimeiroSintoma",
    "label": "Qual a data do surgimento dos primeiros sintomas?"
}

tiposdoencasCronicas = {
    
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
                    "type": "checkbox",
                    "options": [
                        {
                            "label": "Crônica 1",
                        },
                        {
                            "label": "Crônica 2",
                        },
                        {
                            "label": "Outros",
                            "field": {
                                "name": "listaDoencasPacienteField",
                                "placeholder": "Placeholder",
                            },
                        },
                    ]
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
                    "type": "radio",
                    "required": True,
                    "options": [
                        {
                            "label": "ESF 1"
                        },
                        {
                            "label": "ESF 2"
                        }
                    ]
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
    "label": "O Sr/Srª poderia me confirmar seu endereço, por favor? (Caso haja divergências da ficha, anotar abaixo)",
}

qntPessoasMesmoDomicilio = {
    "name": "qntPessoasMesmoDomicilio",
    "label": "Quantas pessoas moram com você?"
}

qualRelacao = {
    "name": "qualRelacao",
    "label": "Qual a sua relação (pai, filho, tio, etc) com cada pessoa que mora com você e idade de cada uma delas?"
}

familiarDoencaCronica = {
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
}

mulherGravida = {
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
                qntPessoasMesmoDomicilio,
                qualRelacao,
                familiarDoencaCronica,
                mulherGravida
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
                    "type": "checkbox",
                    "options": [
                        {
                            "label": "Auxílio 1",
                        },
                        {
                            "label": "Auxílio 2",
                        },
                        {
                            "label": "Outros",
                            "field": {
                                "name": "recebeAuxilioField",
                                "placeholder": "Placeholder",
                            },
                        },
                    ]
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

# Isolamento domiciliar - Lembrar de verificar o fluxo do isolamento domiciliar, proque a parte de manter quarentena aparece duas vezes em dois fluxos diferentes

motivosSairDeCasa = {
    "name": "motivosSairDeCasa",
    "type": "checkbox",
    "label": "Se não: quais são os motivos para sair de casa?",
    "options": [
        {
            "label": "Ir ao supermercado ou a farmácia",
        },
        {
            "label": "Trabalhar",
        },
        {
            "label": "Ir a banco/caixas eletrônicos",
        },
        {
            "label": "Ir a casa de familiares e amigos",
        },
        {
            "label": "Trabalho voluntário",
        },
        {
            "label": "Ir a consultas médicas/fazer exames diagnósticos/tratamentos",
        },
        {
            "label": "Outros",
            "field": {
                "name": "motivosSairDeCasaField",
                "placeholder": "Placeholder",
            },
        },
    ]
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
            "label": "Não",
            "fields": [
                motivosSairDeCasa
            ]
        },
        {
            "label": "Sai só para atividades essenciais (banco, supermercado, etc)."
        }
    ]
}

estrategiaComprarAlimentos = {
    "name": "motivosSairDeCasa",
    "type": "checkbox",
    "label": "Qual tem sido a(s) estratégia(s) usada para a compra de alimentos/medicamentos para o domicílio?",
    "options": [
        {
            "label": "Ida pessoal ao mercado",
        },
        {
            "label": "Entrega em casa (via whatsapp, sites, aplicativos, etc).",
        },
        {
            "label": "Alguém tem feito as compras e deixado no domicílio",
        },
        {
            "label": "Outros",
            "field": {
                "name": "estrategiaCompraAlimentoField",
                "placeholder": "Placeholder",
            },
        },
    ]
}

cuidadoPessoaSairCasa = {
    "name": "cuidadoPessoaSairCasa",
    "label": "Quais são os cuidados que essa pessoa tem tido ao sair de casa para comprar esses itens? E ao chegar em casa? Ou ao receber os produtos?",
    "hint": "Ouvir o relato e orientar medidas de redução de risco da transmissão ao sair e voltar para casa e higienização dos produtos que vem da rua, considerando o contexto socioeconômico do domicílio. Descrever, sucintamente, no campo abaixo, os problemas identificados e/ou orientações passadas ao usuário.",
    "placeholder": "Sua resposta",
    "required": True
}

porqueNaoMantemIsolamento = {
    "label": "Porquê?",
    "name": "porqueNaoMantemIsolamento",
    "hint": "Ouvir o relato e, se for possível, orientar o isolamento. Caso não seja possível o isolamento, orientar estratégias de redução de risco de transmissão. Descrever aqui, sucintamente, os motivos, problemas identificados e/ou orientações fornecidas.",
    "placeholder": "Sua resposta",
}

porqueMantemIsolamento = {
    "label": "Como o Sr/Srª tem feito esse isolamento?",
    "name": "porqueMantemIsolamento",
    "hint": "Ouvir o relato e passar informações adequadas sobre a manutenção do isolamento. Descrever, sucintamente, no campo abaixo, os problemas identificados e/ou orientações passadas ao usuário.",
    "placeholder": "Sua resposta",
}

consegueIsolamentoDomiciliar = {
    "name": "consegueIsolamentoDomiciliar",
    "type": "radio",
    "label": "O Sr/Srª está conseguindo se manter isolado dos demais?",
    "hint": "Manter-se isolado significa estar sozinho em um cômodo da casa, sem acesso aos demais habitantes a esse cômodo. Se o usuário responder não, orientar o isolamento domiciliar, quando possível. Caso não seja possível o isolamento, orientar estratégias de redução de risco de transmissão.",
    "required": True,
    "options": [
        {
            "label": "Sim",
            "fields": [
                porqueMantemIsolamento
            ]
        },
        {
            "label": "Não",
            "fields": [
                porqueNaoMantemIsolamento
            ]
        },
        {
            "label": "Não se aplica, mora sozinho",
            "fields": [
            ]
        }
    ],
}

dormeMesmaCama = {
    "name": "dormeMesmaCama",
    "type": "radio",
    "label": "O Sr/Srª dorme com alguém na mesma cama?",
    "hint": "Se o usuário responder de vez em quando, perguntar se dormiu com alguém na mesma cama nos últimos 15 dias para escolher a alternativa adequada",
    "required": True,
    "options": [
        {
            "label": "Sim"
        },
        {
            "label": "Não"
        }
    ]
}

dormeMesmoQuarto = {
    "name": "dormeMesmoQuarto",
    "type": "radio",
    "label": "E no mesmo quarto?",
    "hint": "Se o usuário responder de vez em quando, perguntar se dormiu com alguém na mesmo quarto nos últimos 15 dias para escolher a alternativa adequada",
    "required": True,
    "options": [
        {
            "label": "Sim"
        },
        {
            "label": "Não"
        }
    ]
}

quemTrabalhaForaDeCasa = {
    "label": "Quem e qual a ocupação?",
    "name": "porqueMantemIsolamento",
    "placeholder": "Sua resposta",
}

cuidadosSairParaTrabalhar = {
    "label": "Quais cuidados têm tomado ao sair para trabalhar? E ao chegar em casa?",
    "name": "cuidadosSairParaTrabalhar",
    "placeholder": "Sua resposta",
    "hint": "Ouvir o relato e orientar medidas de redução de risco da transmissão ao sair e voltar para casa, considerando o contexto socioeconômico do domicílio. Descrever, sucintamente, no campo abaixo, os problemas identificados e/ou orientações passadas ao usuário."
}

alguemTrabalhaForaDeCasa = {
    "name": "alguemTrabalhaForaDeCasa",
    "type": "radio",
    "label": "Algumas das pessoas que mora com você está precisando sair para trabalhar?",
    "required": True,
    "options": [
        {
            "label": "Sim"
        },
        {
            "label": "Não"
        },
        {
            "label": "Não se aplica, mora sozinho",
            "fields": [
                quemTrabalhaForaDeCasa,
                cuidadosSairParaTrabalhar
            ]
        }
    ],
}

# Visitas

quemFoiAVisita = {
    "label": "Quem?",
    "name": "quemFoiAVisita",
    "placeholder": "Sua resposta",
}

porqueRecebeuVisita = {
    "label": "Porquê?",
    "name": "porqueRecebeuVisita",
    "hint": "Após ouvir o relato e considerando o contexto social, econômico e cultural, oriente a não receber visitas em casa e explique o porquê. Caso seja necessário, oriente medidas de redução de risco da transmissão nessas visitas. Descrever, sucintamente, no campo abaixo, o motivo da visita, os problemas identificados e/ou orientações passadas ao usuário.",
    "placeholder": "Sua resposta",
}

recebeuVisita = {
    "name": "recebeuVisita",
    "type": "radio",
    "label": "O Sr/Srª recebeu visitas nos últimos 15 dias?",
    "required": True,
    "options": [
        {
            "label": "Sim",
            "fields": [
                quemFoiAVisita,
                porqueRecebeuVisita
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

# Sintomas COVID 19

apresentouSintomasCovid19 = {
    "name": "apresentouSintomasCovid19",
    "type": "checkbox",
    "label": "O Sr/Srª apresentou algum dos sintomas abaixo nos últimos dias (desde do último atendimento em saúde, por exemplo)?",
    "options": [
        {
            "label": "Febre",
        },
        {
            "label": "Cansaço",
        },
        {
            "label": "Tosse Seca",
        },
        {
            "label": "Mialgia",
        },
        {
            "label": "Fadiga",
        },
        {
            "label": "Congestão Nasal",
        },
        {
            "label": "Dor de Cabeça",
        },
        {
            "label": "Conjutivite",
        },
        {
            "label": "Dor de Garganta",
        },
        {
            "label": "Diarréia",
        },
        {
            "label": "Perda de Paladar ou Olfato",
        },
        {
            "label": "Erupção Cutânea",
        },
        {
            "label": "Descoloração dos Dedos das Mãos e dos Pés",
        },
        {
            "label": "Não apresentou nenhum sintoma",
        },
        {
            "label": "Outros",
            "field": {
                "name": "sintomaCovid19Field",
                "placeholder": "Placeholder",
            },
        },
    ]
}

apresentouFebreQuantosGraus = {
    "label": "Caso tenha apresentado febre, de quanto (anotar o maior número relatado)?",
    "name": "apresentouFebreQuantosGraus",
    "placeholder": "Sua resposta",
}

qualMedicamentoTomou = {
    "label": "Qual?",
    "name": "qualMedicamentoTomou",
    "placeholder": "Sua resposta",
}

quemIndicouMedicamento = {
    "name": "quemIndicouMedicamento",
    "type": "radio",
    "label": "Quem indicou o uso desse medicamento?",
    "required": True,
    "options": [
        {
            "label": "Médico",
        },
        {
            "label": "Enfermeiro"
        },
        {
            "label": "Vizinho/Familiar/Amigo/Conhecido",
        },
        {
            "label": "Dentista"
        },
        {
            "label": "Tomou por conta própria"
        },
        {
            "label": "Outro",
            "fields": [
                {
                    "label": "Quem?",
                    "name": "quemIndicouField",
                    "placeholder": "Placeholder",
                }
            ]
        }
    ],
}

comoTomaMedicamento = {
    "label": "Como está tomando esse(s) medicamento(s)?",
    "hint": "Ouvir o relato e considerando os problemas identificados ou dúvidas, oriente quanto ao uso adequado do medicamentos. Descreva aqui, sucintamente, os problemas identificados, dúvidas e orientações fornecidas.",
    "name": "comoTomaMedicamento",
    "placeholder": "Sua resposta",
}

tomouAlgumMedicamentoProsSintomas = {
    "name": "tomouAlgumMedicamentoProsSintomas",
    "type": "radio",
    "label": "O Sr/Srª tomou algum medicamento para os sintomas que apresentou?",
    "required": True,
    "options": [
        {
            "label": "Sim",
            "fields": [
                qualMedicamentoTomou,
                quemIndicouMedicamento,
                comoTomaMedicamento,
            ]
        },
        {
            "label": "Não"
        },
        {
            "label": "Não se aplica",
        }
    ],
}

quemApresentouSintomas = {
    "label": "Quem?",
    "name": "quemApresentouSintomas",
    "placeholder": "Sua resposta",
}

quaisSintomasApresentou = {
    "name": "quaisSintomasApresentou",
    "type": "radio",
    "label": "Quais sintomas?",
    "required": True,
    "options": [
        {
            "label": "Tosse",
        },
        {
            "label": "Dor de cabeça ou no corpo",
        },
        {
            "label": "Fadiga",
        },
        {
            "label": "Coriza",
        },
        {
            "label": "Dor de garganta",
        },
        {
            "label": "Dificuldade para respirar",
        },
        {
            "label": "Febre",
        },
        {
            "label": "Não apresentou nenhum sintoma",
        },
        {
            "label": "Outros",
            "field": {
                "name": "sintomaCovid19Field",
                "placeholder": "Placeholder",
            },
        },
    ]
}

seFebreDeQuanto = {
    "label": "Se febre, de quanto (anotar o maior número relatado)?",
    "name": "seFebreDeQuanto",
    "placeholder": "Sua resposta",
}

linkNotificacao = {
    "label": "Caso alguém da casa tenha apresentado sintomas, clique aqui para abrir a ficha de notificação: (link)",
    "name": "linkNotificacao",
    "placeholder": "Sua resposta",
}

alguemMaisApresentaSintomaEmCasa = {
    "name": "alguemMaisApresentaSintomaEmCasa",
    "type": "radio",
    "label": "Alguma outra pessoa da sua residência está apresentando algum sintoma de gripe (febre, tosse, dificuldade de respirar, fadiga, dor no corpo, por exemplo)?",
    "required": True,
    "options": [
        {
            "label": "Sim",
            "fields": [
                quemApresentouSintomas,
                quaisSintomasApresentou,
                seFebreDeQuanto,
                linkNotificacao
            ]
        },
        {
            "label": "Não"
        },
        {
            "label": "Não se aplica, mora sozinho",
        }
    ],
}

# Encerramento do Atendimento/Orientações Finais

orientacaoFinal = {
    "name": "orientacaoFinal",
    "type": "checkbox",
    "label": "Orientação final",
    "options": [
        {
            "label": "Encaminhamento para avaliação presencial",
        },
        {
            "label": "Acompanhamento telefônico em 24 horas",
        },
        {
            "label": "Acompanhamento telefônico em 48 horas",
        },
        {
            "label": "Discussão do caso com o supervisor",
        },
        {
            "label": "Contato com o serviço",
        },
        {
            "label": "Outros",
            "field": {
                "name": "outroAtendimentoField",
                "placeholder": "Placeholder",
            },
        },
    ]
}

anotarOrientacoes = {
    "label": "Anotar aqui orientações, dúvidas do atendimento ou qualquer outra informação relevante.",
    "name": "anotarOrientacoes",
    "placeholder": "Sua resposta",
}