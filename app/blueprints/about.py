from flask import Blueprint, render_template
import json

about = Blueprint('About', __name__)

with about.open_resource('../static/json/equipe.json') as f:
    membros = json.load(f)

@about.route('/about', methods=['GET'])
def index():
    return render_template('about.html', membros = membros)