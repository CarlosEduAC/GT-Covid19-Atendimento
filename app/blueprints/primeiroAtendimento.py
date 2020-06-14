from flask import Blueprint, render_template, request, redirect, url_for
from forms.fieldsets import *
from controller.primeiroAtendimento import registrar

primeiroAtendimento = Blueprint('primeiroAtendimento', __name__)


@primeiroAtendimento.route('/primeiroAtendimento', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('form.html', fieldsets=[
            fieldsetConjunto1,
            fieldsetConjunto2,
            fieldsetConjunto3,
            fieldsetConjunto4,
            fieldsetConjunto5,
            fieldsetConjunto6,
        ])
    elif request.method == 'POST':
        dadosFormulario = request.form

        registrar(dadosFormulario)

        return redirect(url_for('primeiroAtendimento.index'))
