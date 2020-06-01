from flask import Blueprint, render_template

from controller.database import Database
from models.modelsAgendamento import Agendamento, Atendimento

menuAtendente = Blueprint('MenuAtendente', __name__)

@menuAtendente.route('/atendente', methods=['GET'])
def index():

    profissional_atual = 1 #ID do profissional acessando

    db = Database()

    agendamentos = Agendamento.query.filter_by(idProfissional = profissional_atual).all()

    atendimentos = []

    for agendamento in agendamentos:
        atendimento = Atendimento.query.filter_by(id = agendamento.idAtendimento).first()
        atendimentos.append(
            {'diaAgendamento':agendamento.dia,
             'primeiro' : atendimento.primeiro,
             'diaAtendimento' : atendimento.dia}
        )

    '''

    atendimentos = [
        {'diaAgendamento':'10/5/2020',
         'primeiro' : True,
         'diaAtendimento' : '10/5/2020'},
        {'diaAgendamento':'10/5/2020',
         'primeiro' : False,
         'diaAtendimento' : '10/5/2020'},
        {'diaAgendamento':'10/5/2020',
         'primeiro' : False,
         'diaAtendimento' : '10/5/2020'},
        {'diaAgendamento':'10/5/2020',
         'primeiro' : True,
         'diaAtendimento' : '10/5/2020'},
    ]
    '''

    return render_template('menuAtendente.html', atendimentos = atendimentos)