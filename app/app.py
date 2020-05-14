from flask import Flask
from flask_cors import CORS
from blueprints.home import home
from blueprints.atendimento import atendimento

app = Flask(__name__)

app.config.from_pyfile('config.py')

app.register_blueprint(home, url_prefix='/')
app.register_blueprint(atendimento, url_prefix='/')

CORS(app)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)