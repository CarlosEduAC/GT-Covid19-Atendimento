from dao.paciente import Paciente
from datetime import datetime
from dao.atendimento import AtendimentoBuilder, inserirPaciente
from flask_login import current_user
import re

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #
# O QUE FALTA: 
# 1- Adicionar doenças cronicas/medicamentos
# 2- Informações dos fieldsets 5 e 6#


def registrar(form):

    # +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #
    #Para testes: essas informações precisam vir por parâmetro
    data=datetime.today()
    #data = datetime.strptime(data, '%d/%m/%Y').date() if len(data) != 0 else None
    id_paciente=1
    id_primeiro_atendimento=None
    
    id_admsaude =current_user.id
    # +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #

    # +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #
    builder = None
    # +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #

    has_atendimento = True if form['has_atendimento'] == '1' else False

    print('has_atendimento: {}'.format(has_atendimento))

    if not has_atendimento:


        # ============ Tentativa ============

        # Comentei algumas coisas porque aparentemente so teremos uma tentativa

        #raw_tentativas = form['tentativas'].split(',')

        # Retorna as chaves da tabela de domínio (list<int>)
        # ex.: [0, 1]
        #real_tentativas = get_real_data(raw_tentativas)
        real_tentativas = data_or_null(form['tentativas'])

        print('real_tentativas: {}'.format(real_tentativas))
        
        # +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #
        builder = AtendimentoBuilder(False, data, id_paciente, tentativa=real_tentativas,
                                        id_atendimento_inicial = id_primeiro_atendimento)
        # +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #

        # Retorna as outras opções que não estão na tabela de domínio (list<str>)
        # ex.: ['Paciente saiu para buscar o filho na escola']
        #others_tentativas = get_others_data(raw_tentativas)

        #print('others_tentativas: {}'.format(others_tentativas))
    else:

        # +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #
        builder = AtendimentoBuilder(False, data, id_paciente,
                                     id_atendimento_inicial = id_primeiro_atendimento)
        # +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #

        # ============== Isolamento domiciliar ==============

        mora_sozinho = data_or_null(form['mora_sozinho'], int)

        print('mora_sozinho: {}'.format(mora_sozinho))

        if mora_sozinho == 2:  # Não
            size = data_or_null(form['mora_sozinho_len'], int)

            parentescos = multiselect(form, 'parentesco', size)

            print('parentescos: {}'.format(parentescos))

            has_parentescos_doenca_cronica = multiselect(form, 'has_parentesco_doenca_cronica', size)

            print('has_parentescos_doenca_cronica: {}'.format(has_parentescos_doenca_cronica))

            parentescos_doenca_cronica = multiselect(form, 'parentesco_doenca_cronica', size)

            print('parentescos_doenca_cronica: {}'.format(parentescos_doenca_cronica))

            parentescos_data_primeiro_sintoma = multiselect(form, 'parentesco_data_primeiro_sintoma', size)

            print('parentescos_data_primeiro_sintoma: {}'.format(parentescos_data_primeiro_sintoma))

            # +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #
            # Falta inserir a doença cronica!!!
            for parentesco in parentescos:
                builder.inserirParentesco(parentesco)
            # +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #



        has_gravida = data_or_null(form['has_gravida'], int)

        print('has_gravida: {}'.format(has_gravida))

        if has_gravida == 1:  # Sim
            gravidas = form['gravida'].split(',')

            print('gravidas: {}'.format(gravidas))

            # +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #
            for gravida in gravidas:
                builder.inserirMulherGravida(gravida)
            # +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #


        # ============== Visitas ==============

        recebeu_visita = data_or_null(form['recebeu_visita'], int)

        print('recebeu_visita: {}'.format(recebeu_visita))

        if recebeu_visita == 1:  # Sim
            size = data_or_null(form['recebeu_visita_len'], int)

            visitas = multiselect(form, 'visita', size)

            print('visitas: {}'.format(visitas))

            pqs_visita = multiselect(form, 'pq_visita', size)

            print('pqs_visita: {}'.format(pqs_visita))

            # +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #
            for visita, motivo in zip(visitas, pqs_visita):
                builder.inserirVisita(visita, motivo)
            # +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #

        # ============== Isolamento domiciliar ==============

        has_isolamento = data_or_null(form['has_isolamento'], int)

        print('has_isolamento: {}'.format(has_isolamento))

        if has_isolamento == 1:  # Sim
            isolamento = data_or_null(form['isolamento'])

            print('isolamento: {}'.format(isolamento))

            # +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #
            builder.inserirIsolamento(True, isolamento)
            # +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #

        elif has_isolamento == 2:  # Não
            nao_isolamento = data_or_null(form['nao_isolamento'])

            print('nao_isolamento: {}'.format(nao_isolamento))

            # +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #
            builder.inserirIsolamento(False, nao_isolamento)
            # +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #

        mantem_quarentena = data_or_null(form['mantem_quarentena'], int)

        print('mantem_quarentena: {}'.format(mantem_quarentena))

        if mantem_quarentena == 1:  # Sim
            dias_quarentena = data_or_null(form['dias_quarentena'], int)

            print('dias_quarentena: {}'.format(dias_quarentena))

            # +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #
            builder.inserirManterEmCasa(True, dias_quarentena)
            # +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #

        elif mantem_quarentena == 2:  # Não
            raw_motivo_sair = form['motivo_sair'].split(',')

            real_motivo_sair = get_real_data(raw_motivo_sair)

            print('real_motivo_sair: {}'.format(real_motivo_sair))

            others_motivo_sair = get_others_data(raw_motivo_sair)

            print('others_motivo_sair: {}'.format(others_motivo_sair))

            # +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #
            builder.inserirManterEmCasa(False)

            for motivo in real_motivo_sair:
                builder.inserirMotivosSair(motivo)#, others_motivo_sair)
            # +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #
    
    # +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #
    builder.finalizarPersistencia(id_admsaude, id_paciente)
    # +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #


def get_real_data(data: list) -> list:
    return list(map(format_real_data, filter(filter_real_data, data)))


def get_others_data(data: list) -> list:
    return list(filter(filter_others_data, data))


def filter_real_data(data: str) -> bool:
    return 'real_data_' in data


def filter_others_data(data: str) -> bool:
    return not filter_real_data(data)


def format_real_data(data: str) -> int:
    return int(data.replace('real_data_', ''))


def data_or_null(data: str, cast=None):
    if cast is None:
        cast = str

    return cast(data) if len(data) != 0 else None


def only_num(data: str):
    if data is None:
        return None

    return re.sub('[^\\d]', '', data)


def multiselect(form, name: str, size) -> list:
    ret = []

    for i in range(1, int(size) + 1):
        name = '{}_{}'.format(name, i).replace('_1', '')
        if name in form:
            ret.append(data_or_null(form[name]))
        else:
            ret.append(None)

    return ret





    