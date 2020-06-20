from flask import Blueprint, render_template, redirect, request, url_for
from datetime import datetime
from dao.paciente import removePaciente, updatePaciente, savePaciente, selectPaciente

registrarPaciente = Blueprint('Paciente', __name__)

@registrarPaciente.route('/paciente', methods=['GET', 'POST'])
def registrar():
    if request.method == 'POST':
        nome = request.form['nome']
        cpf = request.form['cpf']
        sexo = request.form['sexo']
        raca = request.form['raca']
        dataNasc = request.form['data_nasc']
        
        savePaciente(nome, cpf, sexo, raca, datetime.strptime(dataNasc, '%d/%m/%Y'))

    return redirect(url_for('admin.admin'))

@registrarPaciente.route('/paciente/remove', methods=['GET', 'POST'])
def remove():
    if request.method == 'POST':
        id = request.form['paciente_id']

        removePaciente(id)

    return redirect(url_for('admin.admin'))

@registrarPaciente.route('/paciente/update', methods=['GET', 'POST'])
def update():
    if request.method == 'POST':
        id = request.form['paciente_id']
        nome = request.form['nome']
        cpf = request.form['cpf']
        sexo = request.form['sexo']
        raca = request.form['raca']
        dataNasc = request.form['dataNasc']  

        updatePaciente(id, nome, cpf, sexo, raca, dataNasc)    

    return redirect(url_for('admin.admin'))