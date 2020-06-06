from flask import Blueprint, render_template, request, redirect, url_for
from forms.fieldsets import fieldsetConjunto1, fieldsetConjunto2
from controller.primeiroAtendimento import registrar

primeiroAtendimento = Blueprint('primeiroAtendimento', __name__)

@primeiroAtendimento.route('/primeiroAtendimento', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':       
        fieldsets = [
            fieldsetConjunto1,
            fieldsetConjunto2
        ]
        return render_template('form/form.html', fieldsets=fieldsets)
    elif request.method == 'POST':
        dadosFormulario = request.form
        
        registrar(dadosFormulario)

        return redirect(url_for('primeiroAtendimento.index'))
        