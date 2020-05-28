from flask import Blueprint, render_template
from controller.database import Database

home = Blueprint('Home', __name__)

@home.route('/', methods=['GET'])
def index():
    comorbidades = [(1, 'Acima de 60 anos'), (2,'Obesidade'), (3,'Diabetes'),
                    (4, 'Hipertensão'), (5,'Insuficiência Renal'),
                    (6,'Doenças Neurológicas'),(7,'Asma'),(8,'Imunodepressão'),
                    (9,'Puérperas'),(10,'Câncer'),(11,'Outros')]

    return render_template('primeiroAtendimento.html', comorbidades=comorbidades)