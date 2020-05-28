from flask import Blueprint, request, jsonify, redirect, url_for

atendimento = Blueprint('Atendimento', __name__)

@atendimento.route('/atendimento', methods=['POST'])
def index():
    if request.method == 'POST':
        print(request.form)
        # userName = request.form['userName']
        
    return redirect(url_for('Home.index'))