from flask import Blueprint, render_template, redirect, request, url_for
from models.models import AdmSaude
from controller.database import Database

registrarUsuario = Blueprint('Registrar', __name__)

@registrarUsuario.route('/registrar', methods=['GET','POST'])
def registrar():
    if request.method == 'POST':
        nome = request.form['nome']
        CRM = request.form['crm']
        cpf = request.form['cpf']
        
        supervisor = 'supervisor' in request.form

        print(supervisor)
        senha = request.form['senha']
        id = request.form['id']
        
        db = Database()
        
        usuario = AdmSaude(id, nome, CRM, cpf, supervisor, senha)      
        db.saveData(usuario)

        return redirect(url_for('admin.admin'))

    return render_template('registrar.html')