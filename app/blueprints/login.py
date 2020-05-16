from flask import Blueprint, render_template

login = Blueprint('Login', __name__)

@login.route('/login', methods=['GET'])
def index():
    return render_template('login.html')