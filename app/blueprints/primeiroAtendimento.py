from flask import Blueprint, render_template, request, redirect, url_for
from forms.fieldsets import *
from controller.primeiroAtendimento import registrar
from datetime import datetime

primeiroAtendimento = Blueprint('PrimeiroAtendimento', __name__)


@primeiroAtendimento.route('/primeiroAtendimento', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('form.html', fieldsets=[
            fieldsetConjunto0,
            fieldsetConjunto1,
            fieldsetConjunto2,
            fieldsetConjunto3,
            fieldsetConjunto4,
            fieldsetConjunto5,
            fieldsetConjunto6,
        ], now=datetime.today().strftime('%d/%m/%Y'), primeiroAtendimento =True)
    elif request.method == 'POST':
        registrar(request.form)

        return redirect(url_for('PrimeiroAtendimento.index'))
