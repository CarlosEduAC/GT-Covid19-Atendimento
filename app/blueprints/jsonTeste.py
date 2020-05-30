from flask import Blueprint, render_template
import json

teste = Blueprint('Teste', __name__)

with teste.open_resource('../static/json/testePagina.json') as f:
    perguntas = json.load(f)

@teste.route('/teste', methods=['GET'])
def index():
    return render_template('tesjason.html', perguntas = perguntas)