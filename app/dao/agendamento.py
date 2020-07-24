from controller.database import Database
from models.models import Agendamento, Atendimento, Paciente
from datetime import datetime

def userAgendamentos(user_id):
    
    try:
        db = Database()
        session = db.Session()

        return [r._asdict() for r in
            session.query(Agendamento, Atendimento, Paciente).\
            filter(Agendamento.id_atendimento == Atendimento.id,
                    Agendamento.id_adm_saude == user_id,
                    Atendimento.id_paciente == Paciente.id).\
                       order_by(Agendamento.data).\
                           with_entities(Atendimento.id.label('id'),
                                         Paciente.nome.label('nomePaciente'),
                                         Paciente.telefone.label('telefonePaciente'),
                                         Agendamento.data.label('diaAgendamento'),
                                         Atendimento.is_primeiro.label('primeiro'),
                                         Atendimento.data.label('diaAtendimento')).all()]

    except Exception as e:
        print(e)
        return []

