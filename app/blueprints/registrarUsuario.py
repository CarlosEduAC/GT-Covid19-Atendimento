from flask import Blueprint, render_template, redirect, request, url_for, flash
from models.models import AdmSaude
from controller.database import Database
from flask_login import login_required

registrarUsuario = Blueprint('Registrar', __name__)

@registrarUsuario.route('/registrar', methods=['GET','POST'])
@login_required
def registrar():
    if request.method == 'POST':
        nome = request.form['nome']
        CRM = request.form['crm']
        cpf = request.form['cpf']
        
        supervisor = 'supervisor' in request.form

        print(supervisor)
        senha = request.form['senha']
        #id = request.form['id']
        
        db = Database()
        userCPF = db.selectIf(AdmSaude,cpf=cpf)

        if userCPF:
            flash('CPF já cadastrado.')
            return redirect(url_for('Registrar.registrar'))
        
        usuario = AdmSaude(nome, CRM, cpf, supervisor, senha)      
        db.saveData(usuario)

        return redirect(url_for('admin.admin'))

    return render_template('registrar.html')