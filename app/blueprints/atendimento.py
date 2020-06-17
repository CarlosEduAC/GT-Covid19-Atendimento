from flask import Blueprint, render_template, request, redirect, url_for
from forms.fieldsets import *
from controller.atendimento import registrar

atendimento = Blueprint('Atendimento', __name__)

#futuramente, trocar a rota por: /atendimento/<id>
#no index, passar o id por parâmetro
@atendimento.route('/atendimento', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('atendimento.html', fieldsets=[
            fieldsetConjunto4,
            fieldsetConjunto5,
            fieldsetConjunto6
        ])
    elif request.method == 'POST':
        registrar(request.form)
    
        return redirect(url_for('atendimento.index'))