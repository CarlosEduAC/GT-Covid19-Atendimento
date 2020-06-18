from flask import Blueprint, render_template, redirect, request, url_for
from flask_login import login_user, logout_user
from models.models import AdmSaude
from controller.database import Database

login = Blueprint('Login', __name__)

@login.route('/login', methods=['GET', 'POST'])
def loginMetodo():

    if request.method == 'POST':
        cpf = request.form['cpf']
        sh = request.form['senha']

        db = Database()
        
        userCPF = db.selectData(AdmSaude,cpf=cpf) #AdmSaude(7,"maria", 12345678910, 675, 1, sh)

        if not userCPF or not userCPF.verificaSenha(sh):
            return redirect(url_for('login'))
        else:
            login_user(userCPF) 
            return redirect(url_for('MenuAtendente.index'))
    

    return render_template('login.html')
    
@login.route('/logout')
def logout():
    logout_user()
    return render_template('login.html')