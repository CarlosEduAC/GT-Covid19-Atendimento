from flask import Blueprint, render_template, redirect, request, url_for
from models.models import AdmSaude
from controller.database import Database

registrarUsuario = Blueprint('Registrar', __name__)

@registrarUsuario.route('/registrar', methods=['GET','POST'])
def registrar():
    if request.method == 'POST':
        nome = request.form['nome']
        CRM = request.form['crm']
        cargo = request.form['cargo']
        id = request.form['id']
        
        db = Database()
        
        usuario = AdmSaude(nome, CRM, cargo, id)      
        db.saveData(usuario)

    return render_template('registrar.html')