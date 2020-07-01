from controller.database import Database
from models.models import Agendamento, Atendimento


def userAgendamentos(user_id):
    
    try:
        db = Database()
        session = db.Session()

        return session.query(Agendamento, Atendimento).\
            filter(Agendamento.id_atendimento == Atendimento.id and
                   Agendamento.idUsuario == user_id).\
                       order_by(Agendamento.data).\
                           with_entities(Atendimento.id.label('id'),
                                         Agendamento.data.label('diaAgendamento'),
                                         Atendimento.is_primeiro.label('primeiro'),
                                         Atendimento.data.label('diaAtendimento')).all()

    except Exception as e:
        print(e)
        return []

