from flask import Blueprint, render_template
from flask_login import login_required, LoginManager, current_user

from dao.agendamento import userAgendamentos

menuAtendente = Blueprint('MenuAtendente', __name__)

@menuAtendente.route('/', methods=['GET'])
@login_required 
def index():
    atendimentos = userAgendamentos(current_user.id)

    return render_template('menuAtendente.html', atendimentos = atendimentos, usuario=current_user.nome)