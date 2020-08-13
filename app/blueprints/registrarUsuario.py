from flask import Blueprint, render_template, redirect, request, url_for, flash
from models.models import AdmSaude
from controller.database import Database
from controller.primeiroAtendimento import only_num
from flask_login import login_required, current_user
import forms.inputs as inputs
from blueprints.login import ler_dados

registrarUsuario = Blueprint('Registrar', __name__)

@registrarUsuario.route('/registrar', methods=['GET','POST'])
@login_required
def registrar():

    if not (current_user.perfil == 'master' or current_user.perfil == 'admin'):
        return redirect(url_for('MenuAtendente.index'))

    if request.method == 'POST':
        nome = request.form['nome']
        CRM = request.form['crm']
        cpf = only_num(request.form['cpf'])

        if 'cidade' in request.form:
            id_cidade = request.form['cidade']
        else:
            id_cidade = current_user.id_cidade
        
        supervisor = request.form['perfil']

        senha = request.form['senha']
        #id = request.form['id']
        
        db = Database()
        userCPF = db.selectIf(AdmSaude,cpf=cpf)

        if userCPF:
            flash('CPF já cadastrado.')
            return redirect(url_for('Registrar.registrar'))
        
        usuario = AdmSaude(nome, CRM, cpf, supervisor, senha, id_cidade)      
        #if usuario.validarCPF():     
        db.saveData(usuario)

        return redirect(url_for('admin.admin'))
        #else:
        #    flash('CPF inválido.')

    fields = {
        "nome" :inputs.adm_nome,
        "crm" : inputs.adm_crm,
        "cpf" : inputs.adm_cpf,
        "senha" : inputs.adm_senha,
        "cidade" : inputs.cidade
    }

    return render_template('registrar.html', fields=fields, dados = ler_dados(), master=(current_user.perfil == 'master'))