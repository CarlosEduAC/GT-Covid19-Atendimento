from flask import Blueprint, render_template
from flask_login import login_required, LoginManager, current_user

from dao.agendamento import userAgendamentos

menuAtendente = Blueprint('MenuAtendente', __name__)

@menuAtendente.route('/', methods=['GET'])
@login_required 
def index():
    profissional_atual = current_user.id #ID do profissional acessando
    print(current_user.supervisor)

    atendimentos = userAgendamentos(profissional_atual)

    return render_template('menuAtendente.html', atendimentos = atendimentos)