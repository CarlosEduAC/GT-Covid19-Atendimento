from flask import Blueprint, render_template

from dao.agendamento import userAgendamentos

menuAtendente = Blueprint('MenuAtendente', __name__)

@menuAtendente.route('/', methods=['GET'])
def index():
    profissional_atual = 1 #ID do profissional acessando

    atendimentos = userAgendamentos(profissional_atual)

    print(atendimentos)

    return render_template('menuAtendente.html', atendimentos = atendimentos)