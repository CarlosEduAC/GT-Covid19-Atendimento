from flask import Blueprint, render_template
from controller.database import Database
# import models.tables as table

home = Blueprint('Home', __name__)

@home.route('/', methods=['GET'])
def index():
    comorbidades = [(1, 'Acima de 60 anos'), (2,'Obesidade'), (3,'Diabetes'),
                    (4, 'Hipertensão'), (5,'Insuficiência Renal'),
                    (6,'Doenças Neurológicas'),(7,'Asma'),(8,'Imunodepressão'),
                    (9,'Puérperas'),(10,'Câncer'),(11,'Outros')]

    # db = Database()
    # user = table.Usuario('Carlos Eduardo', '09697371490', None, '123456')
    # user2 = table.Usuario('Outra Pessoa', '12345678900', None, '123456')
    # user = table.UsuarioPerfil()
    # user2 = table.UsuarioPerfil(2,1)
    # db.saveData(user)
    # db.saveData(user2)
    return render_template('primeiroAtendimento.html', comorbidades=comorbidades)