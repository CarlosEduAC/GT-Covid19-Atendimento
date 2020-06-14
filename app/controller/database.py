from sqlalchemy import create_engine 
from sqlalchemy.orm import sessionmaker

DATABASE_URL = 'mysql+pymysql://covid:Covid_UFF_UFRJ@10.77.0.29:3306/atendimento_covid_teste'

class Database():
    engine = create_engine(DATABASE_URL, echo=False) # A nossa ponte de conexão entre o Python e o Banco.
    Session = sessionmaker(bind=engine) # Faz um meio de campo entre os objetos que criamos no Python e o engine.
    
    # Salva um objeto específico
    # (data é o objeto que vamos salvar)
    def saveData(self, data): 
        session = self.Session()
        session.add(data)
        session.commit()
    
    # Salva uma lista de dados 
    # (data é o objeto que vamos salvar)
    def saveAll(self, data):
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
            return result
            
    # Retorna um dado específico da Tabela indicada.
    # (model é o Modelo da tabela desejada. Exemplo: Paciente) 
    # (myFilter é a condição desejada. Ex: cpf='1234567890')
    def selectData(self, model, **myFilter): 
        session = self.Session()
        result = session.query(model).filter_by(**myFilter) # .all() .first() . count()

        return result 
    
    # Retorna todas as linhas da Tabela indicada.
    # (model é o Modelo da tabela desejada. Exemplo: Paciente) 
    def selectAllData(self, model): 
        session = self.Session()
        result = session.query(model).all()

        return result

    # Remove um registro pelo id
    def delete(self, model, id):
        session = self.Session()
        result = session.query(model).get(id)

        session.delete(result)
        session.commit()
    