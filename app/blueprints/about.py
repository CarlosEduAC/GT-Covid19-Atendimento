from flask import Blueprint, render_template, request
from json import load
from blueprints.login import ler_dados

about = Blueprint('About', __name__)

@about.route('/about', methods=['GET'])
def index():
    print('here')
    if request.method == 'GET':
        try:
            with about.open_resource('../static/json/equipe.json') as f:
                membros = load(f)
        except Exception as e: 
            membros = None
            print(e)

        return render_template('about.html', membros = membros, dados = ler_dados())