from flask import Blueprint, render_template, request, redirect, url_for
from forms.fieldsets import *
from controller.atendimento import registrar
from dao.atendimento import getInicialPaciente
from dao.paciente import getPaciente
from flask_login import login_required 
from datetime import datetime
from blueprints.login import ler_dados

atendimento = Blueprint('Atendimento', __name__)

# futuramente, trocar a rota por: /atendimento/<id>
# no index, passar o id por parâmetro
@atendimento.route('/atendimento/<id>', methods=['GET', 'POST'])
@login_required
def index(id):
    print("Atendimento inicial: " + id)

    if request.method == 'GET':
        form = {
            "label": "Formulário de Atendimento",
            "desc": "Este é o formulário a ser preenchido nos contatos telefônicos com o usuário",
            "action": "/atendimento/{}".format(id),
        }

        (_, id_paciente) = getInicialPaciente(id)

        paciente = getPaciente(id_paciente)

        fieldsets = [
            preencherPaciente(paciente),
            fieldsetConjunto1,
            fieldsetConjunto4,
            fieldsetConjunto5,
            fieldsetConjunto6
        ]

        return render_template('form.html', form=form, fieldsets=fieldsets, now=datetime.today().strftime('%d/%m/%Y'), dados = ler_dados())
    elif request.method == 'POST':

        (id_inicial, id_paciente) = getInicialPaciente(id)

        #print(str(id_inicial) + " - " + str(id_paciente))

        registrar(request.form, id_inicial, id_paciente)

        return redirect(url_for('MenuAtendente.index'))
