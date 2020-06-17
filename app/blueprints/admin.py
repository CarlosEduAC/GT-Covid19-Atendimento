from flask import Blueprint, render_template, request, redirect, url_for
from controller.admin import getUsers, removeUser, updateUser, getTimes, getEsf, updateTimes, newEsf

menuAdmin = Blueprint('admin', __name__)

@menuAdmin.route('/admin', methods=['GET', 'POST'])
def admin():
    if request.method == 'POST':
        intervalo = request.form['intervalo']
        tempo_maximo = request.form['tempoMaximo']

        updateTimes(intervalo, tempo_maximo)

        return redirect(url_for('admin.admin'))

    elif request.method == 'GET':
        intervalo, tempo_maximo = getTimes() 
        
        esf=getEsf()
        
        """ [
            'Estratégia Saúde da Família - ESF Ajuda A Planalto da Ajuda', 
            'Estratégia Saúde da Família - ESF Ajuda B Ajuda de Baixo',
            'Estratégia Saúde da Família - ESF Ajuda C Ajuda de Cima', 
            'Estratégia Saúde da Família - ESF Areia Branca',
            'Estratégia Saúde da Família - ESF Aroeira'
        ]  """

        users = getUsers()

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
        supervisor = 'supervisor' in request.form

        updateUser(id, name, crm, cpf, supervisor)    

    return redirect(url_for('admin.admin'))

@menuAdmin.route('/admin/esf', methods=['POST'])
def addEsf():
    if request.method == 'POST':
        esf = request.form["esf"]

        newEsf(esf)

    return redirect(url_for('admin.admin'))