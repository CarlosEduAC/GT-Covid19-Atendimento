from flask import Blueprint, render_template, request
from mock import objs
from flask_login import login_required
from sqlalchemy import text
from controller.database import Database

engine = Database().engine

historico = Blueprint('Historico', __name__)


@historico.route('/historico', methods=['GET'])
@login_required
def index():
    id_user = request.args.get('idUsuario')
    section_name = request.args.get('sectionName')
    view = request.args.get('view')
    columns = request.args.get('columns')

    sql = text("SELECT {} FROM {} WHERE id_paciente = {}".format(columns, view, id_user))
    print(sql)
    result = engine.execute(sql)

    result_list = [r for r in result]

    historico = {
        "label": section_name,
        "content": result_list,
        "columns": columns.split(',')
    }

    return render_template('historico.html', historico=historico)
