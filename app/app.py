from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy#####exclir depois testar
from controller.database import Database###excluir depois tirar
from flask_cors import CORS
from blueprints.home import home
from blueprints.login import login
from blueprints.registrarUsuario import registrarUsuario
from blueprints.atendimento import atendimento
from blueprints.menuAtendente import menuAtendente
from blueprints.about import about
from blueprints.form import form
from blueprints.jsonTeste import teste

app = Flask(__name__)
db = SQLAlchemy()

login_manager = LoginManager
#login_manager = LoginManager(app)

app.config.from_pyfile('config.py')

app.register_blueprint(home, url_prefix='/')
app.register_blueprint(login, url_prefix='/')
app.register_blueprint(registrarUsuario, url_prefix='/')
app.register_blueprint(atendimento, url_prefix='/')
app.register_blueprint(menuAtendente, url_prefix='/')
app.register_blueprint(about, url_prefix='/')
app.register_blueprint(form, url_prefix='/')
app.register_blueprint(teste, url_prefix='/')

CORS(app)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)