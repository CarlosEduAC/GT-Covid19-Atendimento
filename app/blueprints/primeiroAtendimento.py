from flask import Blueprint, render_template
from flask import request, jsonify, redirect, url_for
from forms.fieldsets import fieldsetConjunto1, fieldsetConjunto2
#from controller.primeiroAtendimento import registrar
primeiroAtendimento = Blueprint('primeiroAtendimento', __name__)

fieldsets = [
    fieldsetConjunto1,
    fieldsetConjunto2
]


@primeiroAtendimento.route('/primeiroAtendimento', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        #print(request.form)
        registrar(request.form)

    return render_template('form/form.html', fieldsets=fieldsets)
