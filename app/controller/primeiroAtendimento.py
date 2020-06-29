from dao.paciente import Paciente
from datetime import datetime
from dao.atendimento import AtendimentoBuilder
from flask_login import current_user
import re

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #
# O QUE FALTA: 
# 1- Adicionar doenças cronicas/medicamentos
# 2- Campos que não se encontram nos modelos:
# 2.1 - campos de isolamento (consegue manter? pq sim? pq não?
# 2.2 - campos de quarentena (consegue? quantos dias?)
# 2.3 - campos de visita (recebe? quem visitou? pq?)
# 3- Informações dos fieldsets 5 e 6#


def registrar(form):

    # +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #
    #Para testes: essas informações precisam vir po parâmetro
    data=datetime.today()
    #data = datetime.strptime(data, '%d/%m/%Y').date() if len(data) != 0 else None
    id_paciente=1
    id_admsaude =current_user.id
    # +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #

    # +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #
    builder = None
    # +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #

    has_atendimento = True if form['has_atendimento'] == '1' else False

    print('has_atendimento: {}'.format(has_atendimento))

    if not has_atendimento:

        # +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #
        builder = AtendimentoBuilder(True, data, id_paciente, None) #Tem um id para tentativa, mas existem N tentativas..
        # +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #

        # ============ Tentativa ============

        raw_tentativas = form['tentativas'].split(',')

        # Retorna as chaves da tabela de domínio (list<int>)
        # ex.: [0, 1]
        real_tentativas = get_real_data(raw_tentativas)

        print('real_tentativas: {}'.format(real_tentativas))

        # Retorna as outras opções que não estão na tabela de domínio (list<str>)
        # ex.: ['Paciente saiu para buscar o filho na escola']
        others_tentativas = get_others_data(raw_tentativas)

        print('others_tentativas: {}'.format(others_tentativas))
    else:
        # ============== Paciente ==============

        # +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #
        builder = AtendimentoBuilder(True, data, id_paciente)
        # +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #


        nome = data_or_null(form['nome'])
        cpf = data_or_null(form['cpf'], only_num)
        telefone = data_or_null(form['telefone'], only_num)
        endereco = data_or_null(form['endereco'])
        data_nasc = datetime.strptime(form['data_nasc'], '%d/%m/%Y').date() if len(form['data_nasc']) != 0 else None
        id_etnia = data_or_null(form['id_etnia'], int)
        id_genero = data_or_null(form['id_genero'], int)

        print('nome: {}'.format(nome))
        print('cpf: {}'.format(cpf))
        print('telefone: {}'.format(telefone))
        print('endereco: {}'.format(endereco))
        print('data_nasc: {}'.format(data_nasc))
        print('id_etnia: {}'.format(id_etnia))
        print('id_genero: {}'.format(id_genero))

        # ============== Doença Cronica ==============

        has_doenca_cronica = data_or_null(form['has_doenca_cronica'], int)

        if has_doenca_cronica == 1:  # Sim
            size = form['has_doenca_cronica_len']

            # Retorna uma lista com as chaves da tabela de domínio
            # Ex: [1, 2, 4]
            doencas_cronicas = multiselect(form, 'doenca_cronica', size)

            print('doencas_cronicas: {}'.format(doencas_cronicas))

            # Retorna uma lista com as datas do primeiro sintoma da doença.
            # Atenção: o sintoma correspondente está no mesmo índice da variavel [doencas_cronicas]
            datas_primeiro_sintoma = multiselect(form, 'data_primeiro_sintoma', size)

            print('datas_primeiro_sintoma: {}'.format(datas_primeiro_sintoma))

            has_medicamento = multiselect(form, 'has_medicamento', size)

            # +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #
            #for i in size:
                #Adicionar doença cronica

                #builder.adicionarDoencaCronica(doencas_cronicas[i], datas_primeiro_sintoma[i])
            # +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #


        # ============== Medicamento ==============

        has_medicamento = data_or_null(form['has_medicamento'], int)

        print('has_medicamento: {}'.format(has_medicamento))

        if has_medicamento == 1:  # Sim
            size = form['has_medicamento_len']

            medicamentos = multiselect(form, 'medicamento', size)

            print('medicamentos: {}'.format(medicamentos))

            doses_medicamento = multiselect(form, 'dose_medicamento', size)

            print('doses_medicamento: {}'.format(doses_medicamento))

            tempos_medicamento = multiselect(form, 'tempo_medicamento', size)

            print('tempos_medicamento: {}'.format(tempos_medicamento))

            has_indicadores_medicamento = multiselect(form, 'has_indicador_medicamento', size)

            print('has_indicadores_medicamento: {}'.format(has_indicadores_medicamento))

            indicadores_medicamento = multiselect(form, 'indicador_medicamento', size)

            print('indicadores_medicamento: {}'.format(indicadores_medicamento))

        # ============== ESF ==============

        has_estrategia_saude_familiar = data_or_null(form['has_estrategia_saude_familiar'], int)

        print('has_estrategia_saude_familiar: {}'.format(has_estrategia_saude_familiar))

        if has_estrategia_saude_familiar == 1:  # Sim
            raw_estrategias_saude_familiar = form['estrategia_saude_familiar'].split(',')

            real_estrategia_saude_familiar = get_real_data(raw_estrategias_saude_familiar)

            print('real_estrategia_saude_familiar: {}'.format(real_estrategia_saude_familiar))

            others_estrategia_saude_familiar = get_others_data(raw_estrategias_saude_familiar)

            print('others_estrategia_saude_familiar: {}'.format(others_estrategia_saude_familiar))

            # +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #
            for esf in real_estrategia_saude_familiar:
                builder.inserirEstrategiaSaudeFamiliar(esf)
                                                    #others_estrategia_saude_familiar)
            # +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #

        # ============== Domicílio e Auxílios ==============

        qnt_comodos = data_or_null(form['qnt_comodos'], int)

        print('qnt_comodos: {}'.format(qnt_comodos))

        has_agua_encanada = data_or_null(form['has_agua_encanada'], int)

        print('has_agua_encanada: {}'.format(has_agua_encanada))

        
        # +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #
        builder.inserirAtendimentoInicial(qnt_comodos, endereco, has_agua_encanada)
        # +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #


        has_auxilio = data_or_null(form['has_auxilio'], int)

        if has_auxilio == 1:  # Sim
            raw_auxilios = form['auxilio'].split(',')

            real_auxilios = get_real_data(raw_auxilios)

            print('real_auxilios: {}'.format(real_auxilios))

            others_auxilios = get_others_data(raw_auxilios)

            print('others_auxilios: {}'.format(others_auxilios))

            # +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #
            for auxilio in real_auxilios:
                builder.inserirBeneficioSocial(auxilio)#, others_auxilios)
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

        has_gravida = data_or_null(form['has_gravida'], int)

        print('has_gravida: {}'.format(has_gravida))

        if has_gravida == 1:  # Sim
            gravidas = form['gravida'].split(',')

            print('gravidas: {}'.format(gravidas))

        # ============== Visitas ==============

        recebeu_visita = data_or_null(form['recebeu_visita'], int)

        print('recebeu_visita: {}'.format(recebeu_visita))

        if recebeu_visita == 1:  # Sim
            size = data_or_null(form['recebeu_visita_len'], int)

            visitas = multiselect(form, 'visita', size)

            print('visitas: {}'.format(visitas))

            pqs_visita = multiselect(form, 'pq_visita', size)

            print('pqs_visita: {}'.format(pqs_visita))

        # ============== Isolamento domiciliar ==============

        has_isolamento = data_or_null(form['has_isolamento'], int)

        print('has_isolamento: {}'.format(has_isolamento))

        if has_isolamento == 1:  # Sim
            isolamento = data_or_null(form['isolamento'])

            print('isolamento: {}'.format(isolamento))

        elif has_isolamento == 2:  # Não
            nao_isolamento = data_or_null(form['nao_isolamento'])

            print('nao_isolamento: {}'.format(nao_isolamento))

        mantem_quarentena = data_or_null(form['mantem_quarentena'], int)

        print('mantem_quarentena: {}'.format(mantem_quarentena))

        if mantem_quarentena == 1:  # Sim
            dias_quarentena = data_or_null(form['dias_quarentena'], int)

            print('dias_quarentena: {}'.format(dias_quarentena))

        elif mantem_quarentena == 2:  # Não
            raw_motivo_sair = form['motivo_sair'].split(',')

            real_motivo_sair = get_real_data(raw_motivo_sair)

            print('real_motivo_sair: {}'.format(real_motivo_sair))

            others_motivo_sair = get_others_data(raw_motivo_sair)

            print('others_motivo_sair: {}'.format(others_motivo_sair))

            # +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #
            for motivo in real_motivo_sair:
                builder.inserirMotivosSair(motivo)#, others_motivo_sair)
            # +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #
    
    builder.finalizarPersistencia(id_admsaude, id_paciente)


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
