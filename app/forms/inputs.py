from controller.database import Database
from models.modelsDomainTable import *

db = Database()


class Input:
    def __init__(self, name='', type='text', label='', placeholder='', required=False, mask=None, options=None,
                 multiselect=False):
        self.name = name
        self.type = type
        self.label = label
        self.placeholder = placeholder
        self.required = required
        self.mask = mask
        self.options = options
        self.multiselect = multiselect


# =============== Utils ===============

btn_trash = Input(type='btn_trash')

btn_add = Input(type='btn_add')

# ============= Tentativa =============

tentativa = Input(
    type='select',
    name='has_tentativa',
    label='Conseguiu iniciar o atendimento?',
    options=[
        {'value': 'Sim'},
        {'value': 'Não', 'fields': [
            Input(
                type='select',
                name='id_tentativa',
                label='Motivos de falha no contato',
                multiselect=True,
                options=db.selectAllData(Tentativa)
            )
        ]}
    ]
)

# ============== Paciente ==============

nome = Input(
    name='nome',
    label='Nome Completo',
    placeholder='Nome do paciente',
    required=True
)

cpf = Input(
    name='cpf',
    label='CPF',
    placeholder='999.999.999-99',
    mask='999.999.999-99',
    required=True
)

telefone = Input(
    name='telefone',
    label='Telefone',
    mask='(99) 99999999?9',
    placeholder='(99) 999999999'
)

endereco = Input(
    name='endereco',
    label='Endereço',
    placeholder='Rua Recife, 32',
)

data_nasc = Input(
    name='data_nasc',
    label='Data de nascimento',
    mask='99/99/9999',
    placeholder='99/99/9999'
)

etnia = Input(
    type='select',
    name='id_etnia',
    label='Etnia',
    required=True,
    options=db.selectAllData(Etnia)
)

genero = Input(
    type='select',
    name='id_genero',
    label='Gênero',
    required=True,
    options=db.selectAllData(Genero)
)

# Dados básicos


comorbidades = {
    "name": "comorbidades",
    "label": "Comorbidade",
    "type": "select",
    "options": db.selectAllData(DoencaCronica)
}

data_primeiro_sintoma = Input(
    name='data_primeiro_sintoma',
    label='Qual a data do surgimento do primeiro sintoma?',
    mask='99/99/9999',
    placeholder='99/99/9999'
)

tiposdoencasCronicas = {

}

doenca_cronica = Input(
    type='select',
    name='id_doenca_cronica',
    label='Apresenta alguma doença crônica?',
    options=[
        {"value": "Sim", "fields": [[comorbidades, data_primeiro_sintoma, btn_trash], btn_add]},
        {"value": "Não"},
        {"value": "Não opinou"},
    ]
)

medicamentos = {
    "required": True,
    "name": "medicamentos",
    "label": "Qual?",
    "placeholder": "Nome do medicamento",
}

doseRemedioPaciente = {
    "name": "doseRemedioPaciente",
    "label": "Como toma?",
    "placeholder": "Dose, quantidade de vezes ao dia",
    "required": True,
}

tmpRemedioPaciente = {
    "name": "tmpRemedioPaciente",
    "label": "Há quanto tempo?",
    "placeholder": "30 dias"
}

indicador_remedio = {
    "type": "select",
    "required": True,
    "name": "indicador_remedio",
    "label": "Quem?",
    "options": db.selectAllData(Indicador)
}

select_indicador_remedio = {
    "type": "select",
    "name": "select_indicador_remedio",
    "label": "Alguém indicou?",
    "required": True,
    "options": [
        {
            "value": "Sim",
            "fields": [
                indicador_remedio
            ]
        },
        {
            "value": "Não"
        },
        {
            "value": "Não opinou"
        }
    ]
}

toma_medicamento_diariamente = {
    "type": "select",
    "name": "toma_medicamento_diariamente",
    "label": "Toma algum medicamento diariamente?",
    "required": True,
    "options": [
        {
            "value": "Sim",
            "fields": [
                # {
                #     "type": "group"
                # }
                # medicamentos,
                # doseRemedioPaciente,
                # tmpRemedioPaciente,
                # select_indicador_remedio
                # [medicamentos, doseRemedioPaciente, tmpRemedioPaciente, select_indicador_remedio]

                [medicamentos, doseRemedioPaciente, tmpRemedioPaciente, select_indicador_remedio, btn_trash],
                btn_add,
            ]
        },
        {
            "value": "Não"
        },
        {
            "value": "Não opinou"
        }
    ]
}

select_estrategia_saude_familia = {
    "type": "select",
    "name": "select_estrategia_saude_familia",
    "label": "É acompanhado por alguma Estratégia de Saúde da Família?",
    "required": True,
    "options": [
        {
            "value": "Sim",
            "fields": [
                {
                    "type": "select",
                    "multiple": True,
                    "required": True,
                    "name": "estrategia_saude_familia",
                    "label": "Qual?",
                    "options": db.selectAllData(EstrategiaSaudeFamiliar)
                }
            ]
        },
        {
            "value": "Não"
        },
        {
            "value": "Não opinou"
        }
    ]
}

# Domicilio


qnt_pessoas_domicilio = {
    "name": "qnt_pessoas_domicilio",
    "label": "Quantas pessoas moram com você?",
    "mask": "9?9",
    "placeholder": " "
}

qualRelacao = {
    "name": "qualRelacao",
    "label": "Qual a sua relação com cada pessoa que mora com você?"
}

select_mulheres_gravidas = {
    "type": "select",
    "required": True,
    "name": "select_mulheres_gravidas",
    "label": "Caso haja mulheres no domicílio: algumas delas está grávida?",
    "options": [
        {
            "value": "Sim",
            "fields": [
                {
                    "type": "select",
                    "required": True,
                    "multiple": True,
                    "name": "mulheres_gravidas",
                    "label": "Quem?"
                }
            ]
        },
        {
            "value": "Não"
        },
        {
            "value": "Não há mulheres no domicílio"
        }
    ]
}

select_mora_sozinho = {
    "type": "select",
    "required": True,
    "name": "select_mora_sozinho",
    "label": "Mora sozinho?",
    "options": [
        {
            "value": "Sim"
        },
        {
            "value": "Não",
            "fields": [
                qnt_pessoas_domicilio,
                qualRelacao,
                doenca_cronica,
                select_mulheres_gravidas
            ]
        }
    ]
}

# Características do domicílio e auxílios governamentais

qnt_comodos = {
    "name": "qnt_comodos",
    "required": True,
    "label": "Quantos cômodos tem a sua casa?",
    "mask": "9?9",
    "placeholder": " "
}

select_agua_encanada = {
    "type": "select",
    "required": True,
    "name": "select_agua_encanada",
    "label": "Tem acesso a água na torneira de casa?",
    "options": [
        {"value": "Sim"},
        {"value": "Não"}
    ],
}

auxilios = {
    "type": "select",
    "required": True,
    "multiple": True,
    "name": "auxilios",
    "label": "Quais?",
    "options": db.selectAllData(BeneficioSocial),
}

select_auxilios = {
    "type": "select",
    "required": True,
    "name": "select_auxilios",
    "label": "Está recebendo algum auxílio do governo durante esse período da pandemia?",
    "options": [
        {
            "value": "Sim",
            "fields": [auxilios]
        },
        {
            "value": "Não"
        },
        {
            "value": "Já pedi mas ainda não recebi"
        }
    ]
}

# Isolamento domiciliar - Lembrar de verificar o fluxo do isolamento domiciliar, proque a parte de manter quarentena aparece duas vezes em dois fluxos diferentes

motivosSairDeCasa = {
    "type": "select",
    "multiple": True,
    "name": "motivosSairDeCasa",
    "label": "Se não: quais são os motivos para sair de casa?",
    "options": db.selectAllData(MotivoSair),
}

consegueManterQuarentena = {
    "name": "consegueManterQuarentena",
    "type": "select",
    "label": "Você e as pessoas com quem mora estão conseguindo se manter em casa?",
    "required": True,
    "options": [
        {
            "value": "Sim",
            "fields": [
                {
                    "name": "quantosDias",
                    "label": "Há Quantos dias?",
                }
            ]
        },
        {
            "value": "Não",
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

nao_mantem_isolamento = {
    "label": "Porquê?",
    "name": "nao_mantem_isolamento",
    "hint": "Ouvir o relato e, se for possível, orientar o isolamento. Caso não seja possível o isolamento, orientar estratégias de redução de risco de transmissão. Descrever aqui, sucintamente, os motivos, problemas identificados e/ou orientações fornecidas.",
}

mantem_isolamento = {
    "label": "Como tem feito esse isolamento?",
    "name": "mantem_isolamento",
    "hint": "Ouvir o relato e passar informações adequadas sobre a manutenção do isolamento. Descrever, sucintamente, no campo abaixo, os problemas identificados e/ou orientações passadas ao usuário.",
}

select_isolamento_domiciliar = {
    "type": "select",
    "required": True,
    "name": "select_isolamento_domiciliar",
    "label": "Está conseguindo se manter isolado dos demais?",
    "hint": "Manter-se isolado significa estar sozinho em um cômodo da casa, sem acesso aos demais habitantes a esse cômodo. Se o usuário responder não, orientar o isolamento domiciliar, quando possível. Caso não seja possível o isolamento, orientar estratégias de redução de risco de transmissão.",
    "options": [
        {
            "value": "Sim",
            "fields": [
                mantem_isolamento
            ]
        },
        {
            "value": "Não",
            "fields": [
                nao_mantem_isolamento
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

select_recebeu_visitas = {
    "type": "select",
    "required": True,
    "name": "select_recebeu_visitas",
    "label": "Recebeu visitas nos últimos 15 dias?",
    "options": [
        {
            "value": "Sim",
            "fields": [
                quemFoiAVisita,
                porqueRecebeuVisita
            ]
        },
        {
            "value": "Não"
        },
        {
            "value": "Não opinou"
        }
    ]
}

# Sintomas COVID 19

apresentouSintomasCovid19 = {
    "type": "select",
    "multiple": True,
    "name": "apresentouSintomasCovid19",
    "label": "Apresentou algum dos sintomas abaixo nos últimos dias (desde do último atendimento em saúde)?",
    "options": db.selectAllData(Sintoma),
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
    "options": db.selectAllData(Indicador),
}

comoTomaMedicamento = {
    "label": "Como está tomando esse(s) medicamento(s)?",
    "hint": "Ouvir o relato e considerando os problemas identificados ou dúvidas, oriente quanto ao uso adequado do medicamentos. Descreva aqui, sucintamente, os problemas identificados, dúvidas e orientações fornecidas.",
    "name": "comoTomaMedicamento",
    "placeholder": "Sua resposta",
}

tomouAlgumMedicamentoProsSintomas = {
    "name": "tomouAlgumMedicamentoProsSintomas",
    "type": "select",
    "label": "Tomou algum medicamento para os sintomas que apresentou?",
    "required": True,
    "options": [
        {
            "value": "Sim",
            "fields": [
                qualMedicamentoTomou,
                quemIndicouMedicamento,
                comoTomaMedicamento,
            ]
        },
        {
            "value": "Não"
        },
        {
            "value": "Não se aplica",
        }
    ],
}

quemApresentouSintomas = {
    "label": "Quem?",
    "name": "quemApresentouSintomas",
    "placeholder": "Sua resposta",
}

quaisSintomasApresentou = {
    "type": "select",
    "required": True,
    "multiple": True,
    "name": "quaisSintomasApresentou",
    "label": "Quais sintomas?",
    "options": db.selectAllData(Sintoma)
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
    "type": "select",
    "label": "Alguma outra pessoa da sua residência está apresentando algum sintoma de gripe (febre, tosse, dificuldade de respirar, fadiga, dor no corpo, por exemplo)?",
    "required": True,
    "options": [
        {
            "value": "Sim",
            "fields": [
                quemApresentouSintomas,
                quaisSintomasApresentou,
                seFebreDeQuanto,
                linkNotificacao
            ]
        },
        {
            "value": "Não"
        },
        {
            "value": "Não se aplica, mora sozinho",
        }
    ],
}

# Encerramento do Atendimento/Orientações Finais

orientacaoFinal = {
    "type": "select",
    "multiple": True,
    "name": "orientacaoFinal",
    "label": "Orientação final",
    "options": db.selectAllData(OrientacaoFinal),
}

anotarOrientacoes = {
    "label": "Anotar aqui orientações, dúvidas do atendimento ou qualquer outra informação relevante.",
    "name": "anotarOrientacoes",
    "placeholder": "Sua resposta",
}
