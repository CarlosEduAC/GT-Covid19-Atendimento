from flask import Blueprint, render_template
from controller.database import Database
from models.modelsGenerated import Comorbidade
home = Blueprint('Home', __name__)

@home.route('/', methods=['GET'])
def index():
    comorbidades = []
    db = Database()
    comorbidades = db.select(Comorbidade)
    print(comorbidades)

    return render_template('primeiroAtendimento.html', comorbidades=comorbidades)