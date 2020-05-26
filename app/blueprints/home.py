from flask import Blueprint, render_template
from controller.database import Database
import models.models as models

home = Blueprint('Home', __name__)

@home.route('/', methods=['GET'])
def index():
    db = Database()
    # user = table.Usuario('Carlos Eduardo', '09697371490', None, '123456')
    # user2 = table.Usuario('Outra Pessoa', '12345678900', None, '123456')
    # user = table.UsuarioPerfil()
    # user2 = table.UsuarioPerfil(2,1)
    db.saveData(user)
    db.saveData(user2)
    return render_template('home.html')