from controller.database import Database
from models.modelsDomainTable import *

db = Database()


class Input:
    def __init__(self, name='', type='text', label='', placeholder='', required=False, mask=None, options=None,
                 multiselect=False, outros=False, hr=False):
        self.name = name
        self.type = type
        self.label = label
        self.placeholder = placeholder
        self.required = required
        self.mask = mask
        self.options = options
        #-----------------------
        self.hasSelected = False
        self.selected = None
        #-----------------------
        self.multiselect = multiselect
        self.outros = outros
        self.hr = hr
    
    def setValue(self, value):
        if(self.type == 'select'):
            for opt in self.options:
                if opt['id'] == value:
                    opt['selected'] = True
                    self.hasSelected = True
                    self.selected = opt['value']
        else:
            self.value = value
        return self


# =============== Utils ===============

btn_trash = Input(type='btn_trash')

btn_add = Input(type='btn_add')

# ============ Atendimento ============

tentativas = Input(
    type='select',
    name='tentativas',
    label='Motivos de falha no contato',
    options=db.selectAllData(Tentativa),
    outros=True,
)

has_atendimento = Input(
    type='select',
    name='has_atendimento',
    label='Conseguiu iniciar o atendimento?',
    options=[
        {'value': 'Sim'},
        {'value': 'Não', 'fields': [tentativas]}
    ]
)
# ============== AdmSaude ==============

adm_nome = Input(
    name='nome',
    label='Nome Completo',
    placeholder='Nome do Usuário',
    required=True
)

adm_crm = Input(
    name='crm',
    label='CRM',
    placeholder='CRM do Usuário',
    required=True
)

adm_cpf = Input(
    name='cpf',
    label='CPF',
    placeholder='999.999.999-99',
    mask='999.999.999-99',
    required=True
)

adm_senha = Input(
    name='senha',
    label='Senha',
    type='password'
)

adm_is_supervisor = Input(
    name='is_supervisor',
    label='É administrador?',
    type="checkbox"
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
    placeholder='(99) 999999999',
    required=True
)

endereco = Input(
    name='endereco',
    label='Endereço',
    placeholder='Rua Recife, 32',
    required=True
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

# ============== Doença Cronica ==============

doenca_cronica = Input(
    name='doenca_cronica',
    type='select',
    label='Qual?',
    options=db.selectAllData(DoencaCronica)
)

data_primeiro_sintoma = Input(
    name='data_primeiro_sintoma',
    label='Data do diagnóstico?',
    mask='99/99/9999',
    placeholder='99/99/9999'
)

# ============== Medicamento ==============

medicamento = Input(
    name='medicamento',
    label='Medicamento',#'Qual?',
    placeholder='Nome do medicamento'
)

dose_medicamento = Input(
    name='dose_medicamento',
    label='Como toma?',
    placeholder='Dose, quantidade de vezes ao dia',
    required=True
)

tempo_medicamento = Input(
    name='tempo_medicamento',
    label='Há quanto tempo?',
    placeholder='30 dias',
    required=True
)

indicador_medicamento = Input(
    name='indicador_medicamento',
    type='select',
    label='Quem indicou?',
    options=db.selectAllData(Indicador),
    required=True
)

has_indicador_medicamento = Input(
    name='has_indicador_medicamento',
    type='select',
    label='Alguém indicou?',
    required=True,
    options=[
        {"value": "Sim", "fields": [indicador_medicamento]},
        {"value": "Não"},
        {"value": "Não opinou"}
    ]
)

has_medicamento = Input(
    name='has_medicamento',
    type='select',
    label='Toma algum medicamento diariamente?',
    required=True,
    options=[
        {
            'value': 'Sim',
            'fields': [
                [
                    medicamento,
                    dose_medicamento,
                    tempo_medicamento,
                    has_indicador_medicamento,
                    btn_trash
                ],
                btn_add
            ],
        },
        {"value": "Não"},
        {"value": "Não opinou"}
    ]
)

has_doenca_cronica = Input(
    type='select',
    name='has_doenca_cronica',
    label='Apresenta alguma doença crônica?',
    options=[
        {"value": "Sim", "fields": [[doenca_cronica, data_primeiro_sintoma, 
                                     medicamento, indicador_medicamento, 
                                     dose_medicamento, btn_trash], 
                                    btn_add]},
        {"value": "Não"},
        {"value": "Não opinou"},
    ]
)


parentesco_residente_mesma_casa = Input(
    name='parentesco_residente_mesma_casa',
    type='select',
    label='Quem mora com você?',
    options=db.selectAllData(Parentesco)
)

# ============== ESF ==============

estrategia_saude_familiar = Input(
    name='estrategia_saude_familiar',
    type='select',
    multiselect=True,
    label='Qual?',
    options=db.selectAllData(EstrategiaSaudeFamiliar)
)

has_estrategia_saude_familiar = Input(
    name='has_estrategia_saude_familiar',
    type='select',
    label='É acompanhado por alguma Estratégia de Saúde da Família?',
    required=True,
    options=[
        {"value": "Sim", "fields": [estrategia_saude_familiar]},
        {"value": "Não"},
        {"value": "Não opinou"}
    ]
)

# ============== Domicílio e Auxílios ==============

qnt_comodos = Input(
    name='qnt_comodos',
    label='Quantos cômodos tem a sua casa?',
    mask='9?9',
    required=True,
)

has_agua_encanada = Input(
    name='has_agua_encanada',
    type='select',
    label='Tem acesso a água na torneira de casa?',
    options=[
        {"value": "Sim"},
        {"value": "Não"}
    ]
)

auxilio = Input(
    name='auxilio',
    type='select',
    label='Quais?',
    multiselect=True,
    required=True,
    options=db.selectAllData(BeneficioSocial)
)

has_auxilio = Input(
    name='has_auxilio',
    type='select',
    label='Está recebendo algum auxílio do governo durante esse período da pandemia?',
    required=True,
    options=[
        {"value": "Sim", "fields": [auxilio]},
        {"value": "Não"},
        {"value": "Já pedi mas ainda não recebi"}
    ]
)

# ============== Isolamento domiciliar ==============

parentesco = Input(
    name='parentesco',
    type='select',
    label='Qual a relação?',
    options=db.selectAllData(Parentesco)
)

parentesco_doenca_cronica = Input(
    name='parentesco_doenca_cronica',
    type='select',
    label='Qual?',
    options=db.selectAllData(DoencaCronica)
)

parentesco_data_primeiro_sintoma = Input(
    name='parentesco_data_primeiro_sintoma',
    label='Data primeiro sintoma',
    mask='99/99/9999',
    placeholder='99/99/9999'
)

parentesco_doenca_cronica_medicamento = Input(
    type='select',
    name='parentesco_doenca_cronica_medicamento',
    label='Medicamento',
    outros=True,
    options=db.selectAllData(Medicamento)
)

parentesco_doenca_cronica_medicamento_indicador = Input(
    type='select',
    name='parentesco_doenca_cronica_medicamento_indicador',
    label='Quem indicou',
    options=db.selectAllData(Indicador)
)

has_parentesco_doenca_cronica = Input(
    type='select',
    name='has_parentesco_doenca_cronica',
    label='Algum familiar possui doenças crônicas?',
    options=[
        {
            'value': 'Sim',
            'background': '#fafafa',
            'title': 'Doenças Crônicas',
            'fields': [
                [
                    parentesco,
                    parentesco_doenca_cronica,
                    parentesco_data_primeiro_sintoma,
                    parentesco_doenca_cronica_medicamento,
                    parentesco_doenca_cronica_medicamento_indicador,
                    btn_trash
                ],
                Input(type='btn_add', hr=True)
            ]
        },
        {'value': 'Não'}
    ]
)

is_gravida = Input(
    type='select',
    name='is_gravida',
    label='Está gravida?',
    options=[
        {'value': 'Sim'},
        {'value': 'Não'}
    ]
)

parentesco_apresentou_sintoma = Input(
    name='parentesco_apresentou_sintoma',
    type='select',
    label='Qual a relação?',
    options=db.selectAllData(Parentesco)
)

parentesco_sintoma = Input(
    type='select',
    name='parentesco_sintoma',
    label='Sintoma',
    options=db.selectAllData(Sintoma)
)

parentesco_sintoma_medicamento = Input(
    type='select',
    name='parentesco_sintoma_medicamento',
    label='Medicamento',
    options=db.selectAllData(Medicamento),
    outros=True,
)

parentesco_quem_indicou_medicamento = Input(
    type='select',
    name='parentesco_quem_indicou_medicamento',
    label='Quem indicou?',
    options=db.selectAllData(Indicador)
)

parentesco_dosagem = Input(
    name='parentesco_dosagem',
    label='Qual a dosagem?',
)

parentesco_has_sintoma = Input(
    type='select',
    name='parentesco_has_sintoma',
    label='Algum familiar apresentou sintomas nos últimos dias?',
    options=[
        {
            'value': 'Sim',
            'background': '#fafafa',
            'title': 'Medicamentos',
            'fields': [
                [
                    parentesco_apresentou_sintoma,
                    parentesco_sintoma,
                    parentesco_sintoma_medicamento,
                    parentesco_quem_indicou_medicamento,
                    parentesco_dosagem,
                    is_gravida,
                    btn_trash
                ],
                btn_add
            ]
        },
        {'value': 'Não'}
    ]
)

mora_sozinho = Input(
    name='mora_sozinho',
    type='select',
    label='Mora sozinho?',
    required=True,
    options=[
        {"value": "Sim"},
        {
            'value': 'Não',
            "fields": [
                [parentesco_residente_mesma_casa, btn_trash],
                btn_add,
                has_parentesco_doenca_cronica,
                parentesco_has_sintoma,
            ]
        }
    ]
)

# ============== Visitas ==============

visita = Input(
    name='visita',
    label='Quem?',
    placeholder='Sua resposta'
)

pq_vista = Input(
    name='pq_visita',
    label='Porquê?',
    placeholder='Sua resposta'
)

recebeu_visita = Input(
    name='recebeu_visita',
    type='select',
    label='Recebeu visitas nos últimos 15 dias?',
    required=True,
    options=[
        {
            "value": "Sim",
            "fields": [[visita, pq_vista, btn_trash], btn_add]
        },
        {"value": "Não"},
        {"value": "Não opinou"}
    ]
)

# ============== Isolamento domiciliar ==============

isolamento = Input(
    name='isolamento',
    label='Como tem feito esse isolamento?'
)

nao_isolamento = Input(
    name='nao_isolamento',
    label='Porquê?'
)

has_isolamento = Input(
    name='has_isolamento',
    type='select',
    label='Está conseguindo se manter isolado dos demais?',
    required=True,
    options=[
        {"value": "Sim", "fields": [isolamento]},
        {"value": "Não", "fields": [nao_isolamento]}
    ]
)

dias_quarentena = Input(
    name='dias_quarentena',
    label='Há Quantos dias?',
    mask='9?9'
)

motivo_sair = Input(
    name='motivo_sair',
    type='select',
    multiselect=True,
    required=True,
    label='Quais são os motivos para sair de casa?',
    options=db.selectAllData(MotivoSair),
)

mantem_quarentena = Input(
    name='mantem_quarentena',
    type='select',
    label='Todos do domicílio conseguem se manter em casa?',
    required=True,
    options=[
        {"value": "Sim", "fields": [dias_quarentena]},
        {"value": "Não", "fields": [motivo_sair]},
        {"label": "Sai só para atividades essenciais (banco, supermercado, etc)."}
    ]
)

# TODO: Adicionar campo no banco
cuidado_sair_casa = Input(
    name='cuidado_sair_casa',
    label='Cuidados tomados ao sair de casa'
)

# ============== Sintomas COVID 19 ==============

sintoma = Input(
    type='select',
    name='apresentou_sintoma',
    label='Sintoma',
    options=db.selectAllData(Sintoma)
)

sintoma_medicamento = Input(
    name='sintoma_medicamento',
    label='Medicamento',
    placeholder='Nome do medicamento'
)

quem_indicou_medicamento = Input(
    type='select',
    name='quem_indicou_medicamento',
    label='Quem indicou?',
    options=db.selectAllData(Indicador)
)

dosagem = Input(
    name='dosagem',
    label='Observações',
)

has_sintoma = Input(
    type='select',
    name='has_sintoma',
    label='Apresentou algum sintoma nos últimos dias?',
    options=[
        {
            'value': 'Sim',
            'fields': [
                [sintoma, sintoma_medicamento, quem_indicou_medicamento, dosagem, btn_trash],
                btn_add
            ]
        },
        {'value': 'Não'}
    ]
)

# ============== Orientações Finais ==============

orientacao_final = Input(
    type='select',
    name='orientacao_final',
    label='Orientação final',
    options=db.selectAllData(OrientacaoFinal),
    outros=True,
)

anotar_orientacoes = Input(
    name='anotar_orientacoes_finais',
    label='Anotar aqui orientações, dúvidas do atendimento ou qualquer outra informação relevante',
)

# ============== Sobraram esses inputs, o que fazer com eles? ==============

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


linkNotificacao = {
    "label": "Caso alguém da casa tenha apresentado sintomas, clique aqui para abrir a ficha de notificação: (link)",
    "name": "linkNotificacao",
    "placeholder": "Sua resposta",
}
