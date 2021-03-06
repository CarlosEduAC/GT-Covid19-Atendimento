from models.modelsDomainTable import *
from models.modelsAgendamento import *
from controller.database import Database
from models.models import Base, AdmSaude, TempoContatoAcompanhamento

db = Database()

Base.metadata.create_all(bind=db.engine)

# Opcoes Tentativa
db.saveList(Tentativa, [
    "Não atende o telefone",
    "O usuário não estava em casa",
    "O usuário estava em casa mas não disponível para o atendimento",
    "Recusou o atendimento"
])

# Raca
db.saveList(Etnia, [
    "Negra",
    "Amarela",
    "Branca",
    "Parda",
    "Indígena"
])

# Sexo
db.saveList(Genero, [
    "Masculino",
    "Feminino",
    "Não Opinou"
])

# Doencas Cronicas
db.saveList(DoencaCronica, [
    "Diabetes",
    "Hipertensão",
    "Alzheimer",
    "AIDS",
    "Asma",
    "Bronquite",
    "Câncer",
    "Mal de Parkinson",
    "DPOC (Doença Pulmonar Obstrutiva Crônica)",
    "Artrite ou outras doenças reumáticas",
    "Doença renal Crônica",
    "Hanseníase"
])

# Parentesco
db.saveList(Parentesco, [
    "Pai/Mãe",
    "Filho/Filha",
    "Enteado/Enteada",
    "Tio/Tia",
    "Sobrinho/Sobrinha",
    "Avô/Avó",
    "Colega/Amigo/Amiga",
    "Marido/Esposa/Namorado/Namorada",
    "Primo/Prima"
])

# Beneficio Social
db.saveList(BeneficioSocial, [
    "Aposentadoria para pessoa de baixa renda",
    "Auxílio emergencial",
    "Benefícios eventuais (cesta básica emergencial, vale-Feira, auxílio funeral)",
    "Bolsa Família",
    "BPC ( benefício de prestação continuada)",
    "Carteira do Idoso",
    "CNH social",
    "Facultativo baixa renda",
    "ID Jovem",
    "Isenção para serviço ambulante",
    "Minha casa, minha vida",
    "Programa de erradicação do trabalho infantil- PITI",
    "Passe-livre para pessoa com deficiência",
    "Tarifa social de água",
    "Tarifa social de energia elétrica",
    "Não se insere em nenhum programa ou não recebe benefícíos",
    "Não sabe informar"
])

# Motivos para sair de casa
db.saveList(MotivoSair, [
    "Ir ao supermercado ou a farmácia",
    "Trabalhar",
    "Ir a banco/caixas eletrônicos",
    "Ir a casa de familiares e amigos",
    "Trabalho voluntário",
    "Ir a consultas médicas/fazer exames diagnósticos/tratamentos"
])

# Sintomas
db.saveList(Sintoma, [
    "Febre",
    "Cansaço",
    "Tosse Seca",
    "Mialgia",
    "Fadiga",
    "Congestão Nasal",
    "Dor de Cabeça",
    "Conjutivite",
    "Dor de Garganta",
    "Diarréia",
    "Perda de Paladar ou Olfato",
    "Erupção Cutânea",
    "Descoloração dos Dedos das Mãos e dos Pés",
    "Não apresentou nenhum sintoma"
])

# Indicadores de medicamento
db.saveList(Indicador, [
    "Médico",
    "Enfermeiro",
    "Vizinho/Familiar/Amigo/Conhecido",
    "Dentista",
    "Tomou por conta própria"
])

# Orientacoes finais
db.saveList(OrientacaoFinal, [
    "Encaminhamento para avaliação presencial",
    "Acompanhamento telefônico em 24 horas",
    "Acompanhamento telefônico em 48 horas",
    "Discussão do caso com o supervisor",
    "Contato com o serviço"
])

db.saveData(TempoContatoAcompanhamento(
    48, 16
))