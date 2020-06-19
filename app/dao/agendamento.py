from controller.database import Database
from models.models import Agendamento, Atendimento


def userAgendamentos(user_id):
    
    try:
        db = Database()
        session = db.Session()

        return session.query(Agendamento, Atendimento).\
            filter(Agendamento.idAtendimento == Atendimento.id and
                   Agendamento.idUsuario == user_id).\
                       order_by(Agendamento.dia).\
                           with_entities(Atendimento.id.label('id'),
                                         Agendamento.dia.label('diaAgendamento'),
                                         Atendimento.primeiro.label('primeiro'),
                                         Atendimento.dia.label('diaAtendimento')).all()

    except Exception as e:
        print(e)
        return []

