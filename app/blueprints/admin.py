from flask import Blueprint, render_template, request, redirect, url_for
from controller.admin import getUsers, removeUser, updateUser, getTimes, getEsf, deleteEsf, updateTimes, newEsf, genero_etnia, get_cidades
from dao.paciente import getPacientes
from flask_login import login_required, LoginManager, current_user
from blueprints.login import ler_dados

menuAdmin = Blueprint('admin', __name__)

@menuAdmin.route('/admin', methods=['GET', 'POST'])
@login_required
def admin():

    if not (current_user.perfil == 'master' or current_user.perfil == 'admin'):
        return redirect(url_for('MenuAtendente.index'))

    id_cidade = current_user.id_cidade

    if request.method == 'POST':
        intervalo = request.form['intervalo']
        tempo_maximo = request.form['tempoMaximo']

        updateTimes(intervalo, tempo_maximo, id_cidade)

        return redirect(url_for('admin.admin'))

    elif request.method == 'GET':
        intervalo, tempo_maximo = getTimes(id_cidade) 
        
        esf=getEsf(id_cidade)

        users = getUsers(id_cidade)
        pacientes = getPacientes(id_cidade)

        genero, etnia = genero_etnia()
        cidades = get_cidades()

        return render_template('admin.html', users = users, pacientes = pacientes, generos=genero, etnias=etnia,
                                intervalo=intervalo, tempo_maximo=tempo_maximo, esf=esf, dados = ler_dados(), 
                                cidades = cidades, master=(current_user.perfil == 'master'))


@menuAdmin.route('/admin/remove', methods=['GET', 'POST'])
@login_required
def remove():

    if not (current_user.perfil == 'master' or current_user.perfil == 'admin'):
        return redirect(url_for('MenuAtendente.index'))

    if request.method == 'POST':
        id = request.form['user_id']

        removeUser(id)

    return redirect(url_for('admin.admin'))

@menuAdmin.route('/admin/update', methods=['GET', 'POST'])
@login_required
def update():

    if not (current_user.perfil == 'master' or current_user.perfil == 'admin'):
        return redirect(url_for('MenuAtendente.index'))

    if request.method == 'POST':
        id = request.form['user_id']
        name = request.form['nome']
        crm = request.form['crm']
        cpf = request.form['cpf']

        if 'cidade' in request.form:
            id_cidade = request.form['cidade']
            if id_cidade == '0': id_cidade = None
        else:
            id_cidade = current_user.id_cidade

        supervisor = request.form['perfil']
        senha = request.form['senha']

        if senha == "":
            senha = None
       #print("senha: " + senha)

        updateUser(id, name, crm, cpf, supervisor, senha, id_cidade)    

    return redirect(url_for('admin.admin'))

@menuAdmin.route('/admin/esf', methods=['POST'])
@login_required 
def addEsf():

    if not (current_user.perfil == 'master' or current_user.perfil == 'admin'):
        return redirect(url_for('MenuAtendente.index'))

    if request.method == 'POST':
        esf = request.form["esf"]

        newEsf(esf, current_user.id_cidade)

    return redirect(url_for('admin.admin'))

@menuAdmin.route('/admin/esf/<id>', methods=['POST'])
@login_required
def removeEsf(id):

    if not (current_user.perfil == 'master' or current_user.perfil == 'admin'):
        return redirect(url_for('MenuAtendente.index'))
    
    if request.method == 'POST':
        deleteEsf(id)

    return redirect(url_for('admin.admin'))