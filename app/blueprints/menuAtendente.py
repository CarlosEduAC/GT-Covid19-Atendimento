from flask import Blueprint, render_template

menuAtendente = Blueprint('MenuAtendente', __name__)

@menuAtendente.route('/atendente', methods=['GET'])
def index():
    #para testes
    dummyAtendente = [
        {"ultimo":"13/4/2020",
         "status":"quarentena",
         "cond_anteriores":"tosse",
         "mora_sozinho":"sim"},
        {"ultimo":"18/4/2020",
         "status":"quarentena",
         "cond_anteriores":"falta de ar",
         "mora_sozinho":"não"},
        {"ultimo":"1/5/2020",
         "status":"isolado",
         "cond_anteriores":"febre",
         "mora_sozinho":"sim"},
    ]

    return render_template('menuAtendente.html', atendimentos = dummyAtendente)