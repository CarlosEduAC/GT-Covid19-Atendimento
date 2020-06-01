from flask import Blueprint, render_template
import forms.fieldsets as fieldset

form = Blueprint('Test', __name__)

fieldsets = [
    fieldset.fieldsetConjunto1,
    fieldset.fieldsetConjunto2,
]


@form.route('/form', methods=['GET'])
def index():
    return render_template('form/form.html', fieldsets=fieldsets)
