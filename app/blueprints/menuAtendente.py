from flask import Blueprint, render_template

menuAtendente = Blueprint('MenuAtendente', __name__)

@menuAtendente.route('/atendente', methods=['GET'])
def index():
    return render_template('menuAtendente.html')