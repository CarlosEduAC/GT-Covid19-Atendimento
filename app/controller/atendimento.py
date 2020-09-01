from datetime import datetime
from dao.atendimento import AtendimentoBuilder
from dao.paciente import inserirPaciente
from flask_login import current_user
from controller.formfuncs import *

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #

def registrar(form, id_primeiro, id_paciente):

    # +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #
    data=datetime.today()
    # ============== Paciente ==============

    nome = data_or_null(form['nome'])
    cpf = data_or_null(form['cpf'], only_num)
    cns = data_or_null(form['cns'], only_num)
    telefone = data_or_null(form['telefone'], only_num)
    endereco = data_or_null(form['endereco'])
    data_nasc = datetime.strptime(form['data_nasc'], '%d/%m/%Y').date() if len(form['data_nasc']) != 0 else None
    id_etnia = data_or_null(form['id_etnia'], int)
    id_genero = data_or_null(form['id_genero'], int)

    print('nome: {}'.format(nome))
    print('cpf: {}'.format(cpf))
    print('cns: {}'.format(cns))
    print('telefone: {}'.format(telefone))
    print('endereco: {}'.format(endereco))
    print('data_nasc: {}'.format(data_nasc))
    print('id_etnia: {}'.format(id_etnia))
    print('id_genero: {}'.format(id_genero))

    # +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #
    id_paciente = inserirPaciente(nome, cpf, cns, telefone, endereco, data_nasc, id_etnia, id_genero, current_user.id_cidade)
    
    id_admsaude =current_user.id
    # +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #

    # +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #
    builder = None
    # +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #

    print('atendimento: ' + form['has_atendimento'])

    has_atendimento = True if form['has_atendimento'] == '1' else False

    print('has_atendimento: {}'.format(has_atendimento))

    if not has_atendimento:

        # ============ Tentativa ============

        # Comentei algumas coisas porque aparentemente so teremos uma tentativa

        raw_tentativas = form['tentativas'].split(',')

        # Retorna as chaves da tabela de domínio (list<int>)
        # ex.: [0, 1]
        real_tentativas = get_real_data(raw_tentativas)
        # real_tentativas = data_or_null(form['tentativas'])

        print('real_tentativas: {}'.format(real_tentativas))

        # Retorna as outras opções que não estão na tabela de domínio (list<str>)
        # ex.: ['Paciente saiu para buscar o filho na escola']
        others_tentativas = get_others_data(raw_tentativas)

        print('others_tentativas: {}'.format(others_tentativas))

        # +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #
        builder = AtendimentoBuilder(False, data, id_paciente, has_atendimento, id_atendimento_inicial=id_primeiro,
                                        tentativa=real_tentativas, others_tentativas = others_tentativas)
        # +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #
    else:
        
        # +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #
        builder = AtendimentoBuilder(False, data, id_paciente, has_atendimento, id_atendimento_inicial=id_primeiro)
        # +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #

        # ============== Isolamento domiciliar ==============

        mora_sozinho = data_or_null(form['mora_sozinho'], int)

        print('mora_sozinho: {}'.format(mora_sozinho))

        if mora_sozinho == 2:  # Não
            size_parentescos = data_or_null(form['mora_sozinho_len'], int)

            parentescos = multiselect(form, 'parentesco_residente_mesma_casa', size_parentescos)

            print('parentescos: {}'.format(parentescos))

            #Parentesco Doença Cronica
            size_doencas = data_or_null(form['has_parentesco_doenca_cronica_len'], int)

            parentesco = multiselect(form, 'parentesco', size_doencas)

            print('parentesco: {}'.format(parentesco))

            parentesco_doenca_cronica = multiselect(form, 'parentesco_doenca_cronica', size_doencas)

            print('parentesco_doenca_cronica: {}'.format(parentesco_doenca_cronica))

            parentesco_data_primeiro_sintoma = multiselect(form, 'parentesco_data_primeiro_sintoma', size_doencas)

            print('parentesco_data_primeiro_sintoma: {}'.format(parentesco_data_primeiro_sintoma))

            parentesco_doenca_cronica_medicamento = multiselect(form, 'parentesco_doenca_cronica_medicamento', size_doencas)

            print('parentesco_doenca_cronica_medicamento: {}'.format(parentesco_doenca_cronica_medicamento))

            parentesco_doenca_cronica_medicamento_indicador = multiselect(form, 'parentesco_doenca_cronica_medicamento_indicador', size_doencas)

            print('parentesco_doenca_cronica_medicamento_indicador: {}'.format(parentesco_doenca_cronica_medicamento_indicador))

            # +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #
            for i in range(size_doencas):
                if parentesco[i] is None: continue

                if parentesco_data_primeiro_sintoma[i] is None:
                    data = None
                else:
                    data = datetime.strptime(parentesco_data_primeiro_sintoma[i], '%d/%m/%Y').date() \
                        if len(parentesco_data_primeiro_sintoma[i]) != 0 \
                        else None


                builder.inserirParentesco(
                    id_parentesco = parentesco[i], id_doenca_cronica = parentesco_doenca_cronica[i],
                    data_sintomas = data,
                    medicamento = parentesco_doenca_cronica_medicamento[i],
                    id_indicador =  parentesco_doenca_cronica_medicamento_indicador[i])
            # +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #

            #Parentesco Sintomas
            size_sintomas = data_or_null(form['parentesco_has_sintoma_len'], int)

            parentesco_apresentou_sintoma = multiselect(form, 'parentesco_apresentou_sintoma', size_sintomas)

            print('parentesco_apresentou_sintoma: {}'.format(parentesco_apresentou_sintoma))

            parentesco_sintoma = multiselect(form, 'parentesco_sintoma', size_sintomas)

            print('parentesco_sintoma: {}'.format(parentesco_sintoma))

            parentesco_sintoma_medicamento = multiselect(form, 'parentesco_sintoma_medicamento', size_sintomas)

            print('parentesco_sintoma_medicamento: {}'.format(parentesco_sintoma_medicamento))

            parentesco_quem_indicou_medicamento = multiselect(form, 'parentesco_quem_indicou_medicamento', size_sintomas)

            print('parentesco_quem_indicou_medicamento: {}'.format(parentesco_quem_indicou_medicamento))

            parentesco_dosagem = multiselect(form, 'parentesco_dosagem', size_sintomas)

            print('parentesco_dosagem: {}'.format(parentesco_dosagem))

            is_gravida = multiselect(form, 'is_gravida', size_sintomas)

            print('is_gravida: {}'.format(is_gravida))

            # +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #
            for i in range(size_sintomas):
                if  parentesco_apresentou_sintoma[i] is None: continue
                builder.inserirParentesco(
                    id_parentesco = parentesco_apresentou_sintoma[i], is_mulher_gravida = is_gravida[i],
                    id_sintoma = parentesco_sintoma[i], medicamento = parentesco_sintoma_medicamento[i],
                    id_indicador = parentesco_quem_indicou_medicamento[i], dosagem = parentesco_dosagem[i])
            # +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #

            # +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #
            # Aqui sao inseridos apenas os parentescos inseridos que não possuem doenças
            # crônicas nem sintomas
            for p in [item for item in parentescos if item not in parentesco and item not in parentesco_apresentou_sintoma]:
                if p is None: continue
                builder.inserirParentesco(id_parentesco = p)
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
                if visita is None and motivo is None: continue
                builder.inserirVisita(visita, motivo)
            # +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #

        # ============== Isolamento domiciliar ==============

        cuidado_sair_casa = data_or_null(form['cuidado_sair_casa'])

        print('cuidado_sair_casa: {}'.format(cuidado_sair_casa))

        has_isolamento = data_or_null(form['has_isolamento'], int)

        print('has_isolamento: {}'.format(has_isolamento))

        if has_isolamento == 1:  # Sim
            isolamento = data_or_null(form['isolamento'])

            print('isolamento: {}'.format(isolamento))

            # +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #
            builder.inserirIsolamento(True, isolamento, cuidado_sair_casa)
            # +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #

        elif has_isolamento == 2:  # Não
            nao_isolamento = data_or_null(form['nao_isolamento'])

            print('nao_isolamento: {}'.format(nao_isolamento))

            # +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #
            builder.inserirIsolamento(False, nao_isolamento, cuidado_sair_casa)
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
                builder.inserirMotivoSair(motivo)  # , others_motivo_sair)
            # +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #



        # ============== Sintomas COVID ==============

        has_sintomas = data_or_null(form['has_sintoma'], int)

        print('has_sintomas: {}'.format(mantem_quarentena))

        #VERIFICAR COMO ESSAS INFOS ESTÃO VINDO PARA CADASTRAR
        if has_sintomas == 1:  # Sim

            size = data_or_null(form['has_sintoma_len'], int)

            real_sintomas = multiselect(form, 'apresentou_sintoma', size)
            
            real_sintoma_medicamento = multiselect(form, 'sintoma_medicamento', size)

            real_quem_indicou_medicamento = multiselect(form, 'quem_indicou_medicamento', size)

            real_dosagem = multiselect(form, 'dosagem', size)


            for i in range(size):
                if real_sintomas[i] is None: continue
                # +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #
                builder.inserirSintoma(real_sintomas[i], real_sintoma_medicamento[i],
                                        real_quem_indicou_medicamento[i], real_dosagem[i])
                # +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #

        # ============== Orientações Finais ==============

        orientacao_final = format_real_data(form['orientacao_final'])

        print(orientacao_final)

        anotacao_orientacoes = data_or_null(form['anotar_orientacoes_finais'])

        print(anotacao_orientacoes)

        builder.inserirOrientacaoFinal(orientacao_final, anotacao_orientacoes)


    # +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #
    builder.finalizarPersistencia(id_admsaude, id_paciente)
    # +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #