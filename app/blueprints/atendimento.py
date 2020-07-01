from flask import Blueprint, render_template, request, redirect, url_for
from forms.fieldsets import *
from controller.atendimento import registrar
from flask_login import login_required 

atendimento = Blueprint('Atendimento', __name__)

#futuramente, trocar a rota por: /atendimento/<id>
#no index, passar o id por parâmetro
@atendimento.route('/atendimento', methods=['GET', 'POST'])
#@login_required
def index():
    if request.method == 'GET':
        return render_template('atendimento.html', fieldsets=[
            fieldsetConjunto0,
            fieldsetConjunto4,
            fieldsetConjunto5,
            fieldsetConjunto6
        ])
    elif request.method == 'POST':
        registrar(request.form)
    
        return redirect(url_for('atendimento.index'))