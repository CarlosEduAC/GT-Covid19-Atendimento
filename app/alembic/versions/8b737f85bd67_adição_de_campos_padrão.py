"""Adição de campos padrão

Revision ID: 8b737f85bd67
Revises: 0bbd2bfe49df
Create Date: 2020-08-24 17:18:59.244815

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy import orm

from models.modelsDomainTable import *
from models.modelsAgendamento import *
from models.models import *

# revision identifiers, used by Alembic.
revision = '8b737f85bd67'
down_revision = '0bbd2bfe49df'
branch_labels = None
depends_on = None


def upgrade():
    bind = op.get_bind()
    session = orm.Session(bind=bind)

    session.add_all([
        Tentativa("Não atende o telefone"),
        Tentativa("O usuário não estava em casa"),
        Tentativa("O usuário estava em casa mas não disponível para o atendimento"),
        Tentativa("Recusou o atendimento")
    ])

    session.add_all([
        Etnia("Negra"),
        Etnia("Amarela"),
        Etnia("Branca"),
        Etnia("Parda"),
        Etnia("Indígena")
    ])

    session.add_all([
        Genero("Masculino"),
        Genero("Feminino"),
        Genero("Não Opinou")
    ])

    session.add_all([
        DoencaCronica("Diabetes"),
        DoencaCronica("Hipertensão"),
        DoencaCronica("Alzheimer"),
        DoencaCronica("AIDS"),
        DoencaCronica("Asma"),
        DoencaCronica("Bronquite"),
        DoencaCronica("Câncer"),
        DoencaCronica("Mal de Parkinson"),
        DoencaCronica("DPOC (Doença Pulmonar Obstrutiva Crônica)"),
        DoencaCronica("Artrite ou outras doenças reumáticas"),
        DoencaCronica("Doença renal Crônica"),
        DoencaCronica("Hanseníase")
    ])

    session.add_all([
        Parentesco("Pai/Mãe"),
        Parentesco("Filho/Filha"),
        Parentesco("Enteado/Enteada"),
        Parentesco("Tio/Tia"),
        Parentesco("Sobrinho/Sobrinha"),
        Parentesco("Avô/Avó"),
        Parentesco("Colega/Amigo/Amiga"),
        Parentesco("Marido/Esposa/Namorado/Namorada"),
        Parentesco("Primo/Prima")
    ])

    session.add_all([
        BeneficioSocial("Aposentadoria para pessoa de baixa renda"),
        BeneficioSocial("Auxílio emergencial"),
        BeneficioSocial("Benefícios eventuais (cesta básica emergencial, vale-Feira, auxílio funeral)"),
        BeneficioSocial("Bolsa Família"),
        BeneficioSocial("BPC ( benefício de prestação continuada)"),
        BeneficioSocial("Carteira do Idoso"),
        BeneficioSocial("CNH social"),
        BeneficioSocial("Facultativo baixa renda"),
        BeneficioSocial("ID Jovem"),
        BeneficioSocial("Isenção para serviço ambulante"),
        BeneficioSocial("Minha casa, minha vida"),
        BeneficioSocial("Programa de erradicação do trabalho infantil- PITI"),
        BeneficioSocial("Passe-livre para pessoa com deficiência"),
        BeneficioSocial("Tarifa social de água"),
        BeneficioSocial("Tarifa social de energia elétrica"),
        BeneficioSocial("Não se insere em nenhum programa ou não recebe benefícíos"),
        BeneficioSocial("Não sabe informar")
    ])

    session.add_all([
        MotivoSair("Ir ao supermercado ou a farmácia"),
        MotivoSair("Trabalhar"),
        MotivoSair("Ir a banco/caixas eletrônicos"),
        MotivoSair("Ir a casa de familiares e amigos"),
        MotivoSair("Trabalho voluntário"),
        MotivoSair("Ir a consultas médicas/fazer exames diagnósticos/tratamentos")
    ])

    session.add_all([
        Sintoma("Febre"),
        Sintoma("Cansaço"),
        Sintoma("Tosse Seca"),
        Sintoma("Mialgia"),
        Sintoma("Fadiga"),
        Sintoma("Congestão Nasal"),
        Sintoma("Dor de Cabeça"),
        Sintoma("Conjutivite"),
        Sintoma("Dor de Garganta"),
        Sintoma("Diarréia"),
        Sintoma("Perda de Paladar ou Olfato"),
        Sintoma("Erupção Cutânea"),
        Sintoma("Descoloração dos Dedos das Mãos e dos Pés"),
        Sintoma("Não apresentou nenhum sintoma")
    ])

    session.add_all([
        Indicador("Médico"),
        Indicador("Enfermeiro"),
        Indicador("Vizinho/Familiar/Amigo/Conhecido"),
        Indicador("Dentista"),
        Indicador("Tomou por conta própria")
    ])

    session.add_all([
        OrientacaoFinal("Encaminhamento para avaliação presencial"),
        OrientacaoFinal("Acompanhamento telefônico em 24 horas"),
        OrientacaoFinal("Acompanhamento telefônico em 48 horas"),
        OrientacaoFinal("Discussão do caso com o supervisor"),
        OrientacaoFinal("Contato com o serviço")
    ])

    session.add(TempoContatoAcompanhamento(
        48, 16, None
    ))

    session.add(AdmSaude(
        "Dummy User",
        "0101010101",
        "01010101010",
        "master",
        "123456789"
    ))

    session.commit()


def downgrade():
    op.execute("DELETE FROM adms_saude;")
    op.execute("DELETE FROM tempos_contato_acompanhamento;")
    op.execute("DELETE FROM orientacoes_finais;")
    op.execute("DELETE FROM indicadores;")
    op.execute("DELETE FROM sintomas;")
    op.execute("DELETE FROM motivos_sair;")
    op.execute("DELETE FROM beneficios_sociais;")
    op.execute("DELETE FROM parentescos;")
    op.execute("DELETE FROM doencas_cronicas;")
    op.execute("DELETE FROM generos;")
    op.execute("DELETE FROM etnias;")
    op.execute("DELETE FROM tentativas;")
