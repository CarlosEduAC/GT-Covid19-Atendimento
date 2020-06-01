from flask import Blueprint, render_template
#import forms.fieldsets as fieldset
from forms.fieldsets import fieldsetConjunto1,fieldsetConjunto2
form = Blueprint('Test', __name__)

fieldsets = [
    fieldsetConjunto1,
    fieldsetConjunto2,
]


@form.route('/form', methods=['GET'])
def index():
    return render_template('form/form.html', fieldsets=fieldsets)
