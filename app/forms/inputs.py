from controller.database import Database
from models.modelsDomainTable import *

dbHelper = Database()

# Tentativa

opcoesTentativa = {
    "name": "opcoesTentativa",
    "label": "Motivos de falha no contato",
    "type": "select",
    "multiselect": True,
    "outros": {
        "placeholder": "Outro motivo",
        "class": "tagsinput"
    },
    "options": dbHelper.selectAllData(Tentativa)
}

realizaTentativa = {
    "name": "realizaTentativa",
    "label": "Conseguiu iniciar o atendimento?",
    "type": "radio",
    "required": True,
    "options": [
        {
            "label": "Sim",
        },
        {
            "label": "Não",
            "fields": [
               opcoesTentativa
            ]
        }
    ]
}


# Dados básicos

nome = {
    "name": "nome",
    "label": "Nome completo",
    "placeholder": "Nome do paciente",
    "required": True
}

cpf = {
    "name": "cpf",
    "label": "CPF",
    "required": True,
    "mask": "999.999.999-99"
}

telefone = {
    "name": "telefone",
    "label": "Telefone",
    "mask": "(99) 99999999?9",
    "placeholder": "(99) 999999999"
}

aniversario = {
    "type": "date",
    "name": "aniversario",
    "label": "Data de nascimento",
}

sexo = {
    "type": "select",
    "multiselect": False,
    "name": "sexo",
    "label": "Sexo",
    "required": True,
    "options": dbHelper.selectAllData(Genero)
}

raca = {
    "type": "select",
    "multiselect": False,
    "name": "raca",
    "label": "Raça",
    "required": True,
    "options": dbHelper.selectAllData(Etinia)
}

comorbidades = {
    "name": "comorbidades",
    "label": "Comorbidades",
    "type": "select",
    "multiselect": True,
    "outros": {
        "placeholder": "Outras comorbidades",
        "class": "tagsinput"
    },
    "options": dbHelper.selectAllData(DoencaCronica)
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
               comorbidades
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
    "label": "Qual(is)?",
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
    "type": "select",
    "name": "quemIndicouRemedioPaciente",
    "label": "Quem?",
    "required": True,
    "options": dbHelper.selectAllData(Indicador)
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
                    "label": "Qual?",
                    "type": "select",
                    "required": True,
                    "options": dbHelper.selectAllData(EstrategiaSaudeFamiliar)
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
    "label": "Quantas pessoas moram com você?",
    "mask": "9?9",
    "placeholder": "1"
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
                comorbidades
            ]
        },
        {
            "label": "Não"
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
                    "label": "Quem?"
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
    "mask": "9?9",
    "placeholder": "1"
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
                    "type": "select",
                    "options": dbHelper.selectAllData(BeneficioSocial),
                    "multiselect": True
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
    "type": "select",
    "multiselect": True,
    "label": "Se não: quais são os motivos para sair de casa?",
    "options": dbHelper.selectAllData(MotivoSair),
    "outros": {
        "name": "motivosSairDeCasaField",
        "placeholder": "Outros motivos",
        "class": "tagsinput"
    }
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
    "type": "select",
    "multiselect": True,
    "label": "O Sr/Srª apresentou algum dos sintomas abaixo nos últimos dias (desde do último atendimento em saúde, por exemplo)?",
    "options": dbHelper.selectAllData(Sintoma),
    "outros": {
        "name": "sintomaCovid19Field",
        "placeholder": "Outros sintomas",
        "class": "tagsinput"
    }
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
    "type": "select",
    "label": "Quem indicou o uso desse medicamento?",
    "required": True,
    "options": dbHelper.selectAllData(Indicador),
    "outros": {
        "name": "quemIndicouField",
        "placeholder": "Outro indicador",
    }
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
    "type": "select",
    "multiselect": True,
    "label": "Quais sintomas?",
    "required": True,
    "options": dbHelper.selectAllData(Sintoma),
    "outros": {
        "name": "sintomaCovid19Field",
        "placeholder": "Outros sintomas",
        "class": "tagsinput"
    }
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
    "type": "select",
    "multiselect": True,
    "label": "Orientação final",
    "options": dbHelper.selectAllData(OrientacaoFinal),
    "outros": {
        "name": "outroAtendimentoField",
        "placeholder": "Outras orientações finais",
    }
}

anotarOrientacoes = {
    "label": "Anotar aqui orientações, dúvidas do atendimento ou qualquer outra informação relevante.",
    "name": "anotarOrientacoes",
    "placeholder": "Sua resposta",
}
