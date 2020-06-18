from flask import Blueprint, render_template
from flask_login import login_required, LoginManager

from dao.agendamento import userAgendamentos

menuAtendente = Blueprint('MenuAtendente', __name__)

@menuAtendente.route('/', methods=['GET'])
@login_required #só permite acessar esta pagina sé estiver logado

def index():
    profissional_atual = 1 #ID do profissional acessando

    atendimentos = userAgendamentos(profissional_atual)

    return render_template('menuAtendente.html', atendimentos = atendimentos)