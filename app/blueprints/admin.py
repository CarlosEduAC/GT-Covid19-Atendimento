from flask import Blueprint, render_template, request, redirect, url_for
from controller.admin import getUsers, removeUser, updateUser

menuAdmin = Blueprint('admin', __name__)

@menuAdmin.route('/admin', methods=['GET', 'POST'])
def admin():
    if request.method == 'POST':

        intervalo = request.form['intervalo']
        tempo_maximo = request.form['tempoMaximo']

        #Alterar no banco esses dados

        return render_template('admin.html')

    elif request.method == 'GET':

        intervalo, tempo_maximo = (48, 12) #Fazer consulta ao banco para recuperar esses dados
        
        esf=['opt1', 'opt2']

        users = getUsers()
        #adms = getAdms()

        return render_template('admin.html', users = users, 
                                intervalo=intervalo, tempo_maximo=tempo_maximo, esf=esf)


@menuAdmin.route('/admin/remove', methods=['GET', 'POST'])
def remove():


    if request.method == 'POST':

        id = request.form['user_id']

        removeUser(id)

    return redirect(url_for('admin.admin'))

@menuAdmin.route('/admin/update', methods=['GET', 'POST'])
def update():

    if request.method == 'POST':

        id = request.form['user_id']
        name = request.form['nome']
        crm = request.form['crm']
        cpf = request.form['cpf']                
        supervisor = request.form['supervisor']

        updateUser(id, name, crm, cpf, supervisor)    

    return redirect(url_for('admin.admin'))
