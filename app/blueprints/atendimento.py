from flask import Blueprint, request, jsonify, redirect, url_for
import controller.database as db
atendimento = Blueprint('Atendimento', __name__)

@atendimento.route('/atendimento', methods=['POST'])
def index():
    if request.method == 'POST':
        userName = request.form['userName']
        # db.Database()
    return redirect(url_for('Home.index'))