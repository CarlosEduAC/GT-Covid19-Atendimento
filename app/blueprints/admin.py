from flask import Blueprint, render_template, request, redirect, url_for
from controller.admin import getUsers, removeUser, updateUser, getTimes, getEsf, deleteEsf, updateTimes, newEsf, genero_etnia
from dao.paciente import getPacientes
from flask_login import login_required, LoginManager, current_user
from blueprints.login import ler_dados

menuAdmin = Blueprint('admin', __name__)

@menuAdmin.route('/admin', methods=['GET', 'POST'])
@login_required
def admin():

    if not current_user.is_supervisor:
        return redirect(url_for('MenuAtendente.index'))

    if request.method == 'POST':
        intervalo = request.form['intervalo']
        tempo_maximo = request.form['tempoMaximo']

        updateTimes(intervalo, tempo_maximo)

        return redirect(url_for('admin.admin'))

    elif request.method == 'GET':
        intervalo, tempo_maximo = getTimes() 
        
        esf=getEsf()

        users = getUsers()
        pacientes = getPacientes()

        genero, etnia = genero_etnia()

        return render_template('admin.html', users = users, pacientes = pacientes, generos=genero, etnias=etnia,
                                intervalo=intervalo, tempo_maximo=tempo_maximo, esf=esf, dados = ler_dados())


@menuAdmin.route('/admin/remove', methods=['GET', 'POST'])
@login_required
def remove():

    if not current_user.is_supervisor:
        return redirect(url_for('MenuAtendente.index'))

    if request.method == 'POST':
        id = request.form['user_id']

        removeUser(id)

    return redirect(url_for('admin.admin'))

@menuAdmin.route('/admin/update', methods=['GET', 'POST'])
@login_required
def update():

    if not current_user.is_supervisor:
        return redirect(url_for('MenuAtendente.index'))

    if request.method == 'POST':
        id = request.form['user_id']
        name = request.form['nome']
        crm = request.form['crm']
        cpf = request.form['cpf']                
        supervisor = 'is_supervisor' in request.form
        senha = request.form['senha']

        if senha == "":
            senha = None
       #print("senha: " + senha)

        updateUser(id, name, crm, cpf, supervisor, senha)    

    return redirect(url_for('admin.admin'))

@menuAdmin.route('/admin/esf', methods=['POST'])
@login_required 
def addEsf():

    if not current_user.is_supervisor:
        return redirect(url_for('MenuAtendente.index'))

    if request.method == 'POST':
        esf = request.form["esf"]

        newEsf(esf)

    return redirect(url_for('admin.admin'))

@menuAdmin.route('/admin/esf/<id>', methods=['POST'])
@login_required
def removeEsf(id):

    if not current_user.is_supervisor:
        return redirect(url_for('MenuAtendente.index'))
    
    if request.method == 'POST':
        deleteEsf(id)

    return redirect(url_for('admin.admin'))