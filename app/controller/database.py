from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sys

if len(sys.argv) == 1: # Banco de dados de produção
    DATABASE_URL = 'mysql+pymysql://covid:Covid_UFF_UFRJ@10.77.0.29:3306/atendimento_covid_teste'
else:
    if 'dev' in sys.argv[1].lower(): # Banco de dados local
        DATABASE_URL = 'mysql+pymysql://root:123456@localhost:3306/covid3'
    else: # Banco de dados de teste
        DATABASE_URL = 'mysql+pymysql://covid:Covid_UFF_UFRJ@10.77.0.29:3306/atendimento_covid_teste'

class Database:
    engine = create_engine(DATABASE_URL, echo=False)  # A nossa ponte de conexão entre o Python e o Banco.
    Session = sessionmaker(bind=engine)  # Faz um meio de campo entre os objetos que criamos no Python e o engine.

    # Salva um objeto específico
    # (data é o objeto que vamos salvar)
    def saveData(self, data) -> None:
        session = self.Session()
        session.add(data)
        session.commit()

    # Salva objetos a partir de uma lista
    # (dataList é a lista de objetos que vamos salvar)
    def saveList(self, model, dataList) -> None:
        for elem in dataList:
            self.saveData(model(elem))

    # Salva uma lista de dados
    # (data é o objeto que vamos salvar)
    def saveAll(self, data) -> None:
        session = self.Session()
        session.add_all(data)
        session.commit()

    # Retorna um objeto do banco se já existir, caso contrario antes do retorno cria o objeto
    # (model é o Modelo da tabela desejada. Exemplo: Paciente) 
    # (myFilter é a condição desejada. Ex: cpf='1234567890') 
    # (data é o objeto que vamos valvar)
    def saveIfNew(session, model, data, **myFilter):
        result = session.query(model).filter_by(**myFilter).first()
        if result:
            return result
        else:
            result = model(data)
            session.add(result)
            session.commit()
            return [r.to_dict() for r in result]

    # Retorna a primeira linha da Tabela indicada.
    # (model é o Modelo da tabela desejada. Exemplo: Paciente) 
    def selectData(self, model):
        session = self.Session()
        result = session.query(model).first()

        return result

    def selectIf(self, model, **myfilter):
        session = self.Session()
        result = session.query(model).filter_by(**myfilter).first()

        return result

    # Retorna todas as linhas da Tabela indicada.
    # (model é o Modelo da tabela desejada. Exemplo: Paciente) 
    def selectAllData(self, model):
        session = self.Session()
        result = session.query(model).all()

        return [r.to_dict() for r in result]

    def selectAllDataFilter(self, model, myfilter):
        # myfilter = nome='Carlos', idade=15
        session = self.Session()
        result = session.query(model).filter(myfilter).all()

        return [r.to_dict() for r in result]

    def selectAllDataByFilter(self, model, **myfilter):
        # **myfilter = {'nome': 'Carlos', 'idade': 15} => nome='Carlos', idade=15
        session = self.Session()
        result = session.query(model).filter_by(**myfilter).all()

        return [r.to_dict() for r in result]

    # Remove um registro pelo id
    def delete(self, model, id) -> None:
        session = self.Session()
        result = session.query(model).get(id)

        session.delete(result)
        session.commit()

    def updateData(self, model, dataUpdate, id) -> None:
        session = self.Session()
        data = session.query(model).get(id)
        session.merge(dataUpdate)
        session.commit()
