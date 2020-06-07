from flask import Blueprint, render_template

from controller.agendamentoDao import userAgendamentos

menuAtendente = Blueprint('MenuAtendente', __name__)

@menuAtendente.route('/atendente', methods=['GET'])
def index():

      
    profissional_atual = 1 #ID do profissional acessando

    atendimentos = userAgendamentos(profissional_atual)

    print(atendimentos)

    return render_template('menuAtendente.html', atendimentos = atendimentos)