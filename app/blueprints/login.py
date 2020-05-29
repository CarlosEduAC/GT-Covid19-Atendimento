from flask import Blueprint, render_template, redirect, request, url_for
from models.models import AdmSaude
from controller.database import Database

login = Blueprint('Login', __name__)

@login.route('/login', methods=['GET'])
def index():
    return render_template('login.html')
    
@login.route('/logout', methods=['GET'])
def logout():
    return render_template('login.html')