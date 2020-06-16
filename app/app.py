# Importações básicas
from flask import Flask
from flask_cors import CORS

# Importação de rotas 
from blueprints.about import about
from blueprints.login import login
from blueprints.admin import menuAdmin
from blueprints.atendimento import atendimento
from blueprints.menuAtendente import menuAtendente
from blueprints.registrarUsuario import registrarUsuario
from blueprints.registrarPaciente import registrarPaciente
from blueprints.primeiroAtendimento import primeiroAtendimento

app = Flask(__name__)

app.config.from_pyfile('config.py')

app.register_blueprint(about, url_prefix='/')
app.register_blueprint(login, url_prefix='/')
app.register_blueprint(menuAdmin, url_prefix='/')
app.register_blueprint(atendimento, url_prefix='/')
app.register_blueprint(menuAtendente, url_prefix='/')
app.register_blueprint(registrarUsuario, url_prefix='/')
app.register_blueprint(registrarPaciente, url_prefix='/')
app.register_blueprint(primeiroAtendimento, url_prefix='/')

CORS(app)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)