from flask import Blueprint, render_template, request, redirect, url_for
from forms.fieldsets import *
from controller.atendimento import registrar
from datetime import datetime

atendimento = Blueprint('Atendimento', __name__)


# futuramente, trocar a rota por: /atendimento/<id>
# no index, passar o id por parâmetro
@atendimento.route('/atendimento', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        form = {
            "label": "Formulário de Atendimento",
            "desc": "Este é o formulário a ser preenchido nos contatos telefônicos com o usuário",
            "action": "/atendimento",
        }

        fieldsets = [
            fieldsetConjunto0,
            fieldsetConjunto4,
            fieldsetConjunto5,
            fieldsetConjunto6
        ]

        return render_template('form.html', form=form, fieldsets=fieldsets, now=datetime.today().strftime('%d/%m/%Y'))
    elif request.method == 'POST':
        registrar(request.form)

        return redirect(url_for('atendimento.index'))
