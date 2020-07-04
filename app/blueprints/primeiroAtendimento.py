from flask import Blueprint, render_template, request, redirect, url_for
from forms.fieldsets import *
from controller.primeiroAtendimento import registrar
from datetime import datetime
from flask_login import login_required

primeiroAtendimento = Blueprint('PrimeiroAtendimento', __name__)


@primeiroAtendimento.route('/primeiroAtendimento', methods=['GET', 'POST'])
@login_required
def index():
    if request.method == 'GET':
        form = {
            "label": "Formulário Primeiro Atendimento",
            "desc": "Este é o formulário a ser preenchido no primeiro contato telefônico com o usuário",
            "action": "/primeiroAtendimento",
            "primeiroAtendimento": True,
        }

        fieldsets = [
            fieldsetConjunto0,
            fieldsetConjunto1,
            fieldsetConjunto2,
            fieldsetConjunto3,
            fieldsetConjunto4,
            fieldsetConjunto5,
            # fieldsetConjunto6,
        ]

        return render_template('form.html', form=form, fieldsets=fieldsets, now=datetime.today().strftime('%d/%m/%Y'))
    elif request.method == 'POST':
        #print(request.form)
        registrar(request.form)

        return redirect(url_for('PrimeiroAtendimento.index'))
