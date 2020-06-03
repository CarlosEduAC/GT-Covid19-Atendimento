from flask import Blueprint, render_template
from forms.fieldsets import fieldsetConjunto1, fieldsetConjunto2
primeiroAtendimento = Blueprint('primeiroAtendimento', __name__)

fieldsets = [
    fieldsetConjunto1,
    fieldsetConjunto2,
]


@primeiroAtendimento.route('/primeiroAtendimento', methods=['GET'])
def index():
    return render_template('form/form.html', fieldsets=fieldsets)
