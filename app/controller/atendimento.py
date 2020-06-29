from dao.paciente import Paciente
from datetime import datetime
from dao.atendimento import AtendimentoBuilder

def registrarCamposComuns(builder, form):
    #Adicionar parentesco/domicilio aqui
    return

    


def registrar(formulario):

    print(formulario)

def registrarPrimeiro(form, data, paciente):

    if form["realizaTentativa"]: #==1?
        for tentativa in form.getlist('opcoesTentativa'):
            print(tentativa)
        builder = AtendimentoBuilder(True, data, paciente, tentativa="Valor da tentativa aqui")
    else:
        builder = AtendimentoBuilder(True, data, paciente)

        endereco = form["endereco"]
        qtd_comodos = form["qntComodos"]
        is_agua_encanada = form["aguaEncanada"]

        builder.inserirAtendimentoInicial(endereco, qtd_comodos, is_agua_encanada)

        if form["esf"]: #==1?
            esf = form["esfDescricao"]

            builder.adicionarEstrategiaSaudeFamiliar(esf)
        
        #Adicionar doenças cronicas aqui


    




    