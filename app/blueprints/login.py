from flask import Blueprint, render_template, redirect, request, url_for, flash
from flask_login import login_user, logout_user, login_required 
from models.models import AdmSaude
from controller.database import Database
from json import load

login = Blueprint('Login', __name__)

def ler_dados():
    try:
        with login.open_resource('../static/json/dadosCliente.json') as f:
            dados = load(f)
            return dados

    except Exception as e: 
        dados = None
        print(e)

@login.route('/login', methods=['GET', 'POST'])
def loginMetodo():

    if request.method == 'GET':
        
        dados = ler_dados()

        return render_template('login.html', dados = dados)           
    
    elif request.method == 'POST':
        cpf = request.form['cpf']
        sh = request.form['senha']

        db = Database()
        
        userCPF = db.selectIf(AdmSaude,cpf=cpf) 

        print(userCPF)
        if not userCPF or not userCPF.verificaSenha(sh):
            flash('Dados inválidos.')
            return redirect(url_for('Login.loginMetodo'))
        else:
            login_user(userCPF) 
            return redirect(url_for('MenuAtendente.index'))
    
@login.route('/logout')
@login_required 
def logout():
    logout_user()
    return redirect(url_for('Login.loginMetodo'))