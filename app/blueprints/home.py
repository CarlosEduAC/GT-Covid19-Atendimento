from flask import Blueprint, render_template

home = Blueprint('Home', __name__)

@home.route('/', methods=['GET'])
def index():
    return render_template('home.html')