from flask import Blueprint, request, jsonify, redirect, url_for

atendimento = Blueprint('Atendimento', __name__)

@atendimento.route('/atendimento', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        userName = request.form['userName']

    return redirect(url_for('Home.index'))

    #return jsonify({'Nome': userName})