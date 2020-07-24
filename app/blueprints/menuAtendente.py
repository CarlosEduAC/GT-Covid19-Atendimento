from flask import Blueprint, render_template
from flask_login import login_required, LoginManager, current_user
from datetime import datetime
from flask_weasyprint import HTML, render_pdf

from dao.agendamento import userAgendamentos

menuAtendente = Blueprint('MenuAtendente', __name__)

@menuAtendente.route('/', methods=['GET'])
@login_required 
def index():
    atendimentos = list(map(
        setImportance, 
        userAgendamentos(current_user.id)))

    return render_template('menuAtendente.html', atendimentos = atendimentos, formatTime = datetime.strftime, pdf = False)

@menuAtendente.route('/pdf', methods=['GET'])
@login_required 
def indexPDF():
    atendimentos = list(map(
        setImportance, 
        userAgendamentos(current_user.id)))

    template_renderizado = render_template('agendamento.html', atendimentos = atendimentos, formatTime = datetime.strftime, pdf = True)

    return render_pdf(HTML(string=template_renderizado))


def setImportance(atendimento):
    today = datetime.today().date()
    time = atendimento['diaAgendamento'].date()
    
    if(today > time):
        atendimento['importance'] = 1
    elif(today == time):
        atendimento['importance'] = 2
    else:
        atendimento['importance'] = 3
    
    return atendimento
