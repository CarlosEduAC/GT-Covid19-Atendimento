from flask import Blueprint, render_template, redirect, request, url_for
from datetime import datetime
from controller.database import Database
from models.models import Paciente

registrarPaciente = Blueprint('Paciente', __name__)

@registrarPaciente.route('/paciente', methods=['GET', 'POST'])
def registrar():

    if request.method == 'POST':
        nome = request.form['nome']
        cpf = request.form['cpf']
        ocupacao = request.form['ocupacao']
        sexo = request.form['sexo']
        raca = request.form['raca']
        dataNasc = request.form['data_nasc']

        paciente = Paciente(nome, cpf, ocupacao, sexo, raca, datetime.strptime(dataNasc, '%d/%m/%Y'))

        db=Database()
        db.saveData(paciente)
    
    return render_template('paciente.html')

