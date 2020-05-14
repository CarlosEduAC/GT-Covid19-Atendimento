from flask import Blueprint, request, jsonify, render_template

atendimento = Blueprint('Atendimento', __name__)

@atendimento.route('/atendimento', methods=['POST'])
def index():
    if request.method == 'POST':
        userName = request.form['userName']

        return render_template('home.html')

    #return jsonify({'Nome': userName})