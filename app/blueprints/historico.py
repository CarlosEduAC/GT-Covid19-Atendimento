from flask import Blueprint, render_template, request
from mock import objs
from flask_login import login_required

historico = Blueprint('Historico', __name__)

@historico.route('/historico', methods=['GET'])
#@login_required
def index():

    idUsuario = request.args.get('idUsuario')
    inputName = request.args.get('inputName')
    label = request.args.get('label')
    
    historico = {
        "label": label,
        "content": [
            {
                "date": "16/03/2020",
                "value": objs.atendimento[inputName]
            },
            {
                "date": "16/03/2020",
                "value": objs.atendimento[inputName]
            }
        ]
    }

    return render_template('historico.html', historico = historico)

