from flask import Blueprint, render_template
from flask import request, jsonify, redirect, url_for
from forms.fieldsets import *
#from controller.primeiroAtendimento import registrar
primeiroAtendimento = Blueprint('primeiroAtendimento', __name__)

fieldsets = [
    fieldsetConjunto1,
    fieldsetConjunto2,
    fieldsetConjunto3
]


@primeiroAtendimento.route('/primeiroAtendimento', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        #print(request.macros)
        registrar(request.form)

    return render_template('macros/macros.html', fieldsets=fieldsets)
