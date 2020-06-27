from controller.database import Database
from models.models import Atendimento, AtendimentoInicial, Agendamento


class AtendimentoBuilder(): #Incluir funções de cadastro de outras tabelas

    #Classe de atendimento que será moficada aos poucos
    self.atendimento = Atendimento()

    #Essas listas conterão informações que dependem do atendimento estar
    #cadastrado (ja que precisarão do ID dele para serem inseridas no
    # banco). Ao fim do cadastro das informações do atendimento, essas listas
    # serão percorridas e os dados nelas cadastrados.
    self.comorbidades = []
    self.doencas_cronicas = []
    self.medicamentos = []
    self.auxilios = []
    self.pessoas_domicilio = []
    self.motivos_sair = []
    self.sintomas_covid = []
    self.medicamentos_sintomas = []
    self.sintomas_familiar = []
    self.orientacoes_finais = []

    #Se não for o atendimento inicial, passa o id do inicial no construtor
    #No construtor, passar também o dia do atendimento
    def __init__(self, dia, idInicial=None):
        self.atendimento.dia = dia
        if idInicial is not None:
            self.atendimento.idInicial = idInicial
            self.atendimento.primeiro = False
    

    #Aqui são cadastradas as informações do atendimento inicial, caso esse atendimento seja o inicial
    def cadastrarInicial(self, endereco, idPaciente, esf, qtdComodos, aguaEncanada,
                            opinouDoencaCronica=None, opinouRemedio=None, opinouEsf = None, pediuAuxilio=None):
        if self.idInicial is not None: #Se já houver um atendimento inicial, não deixa cadastrar outro por cima
            return
        
        inicial = AtendimentoInicial()

        inicial.endereco = endereco
        inicial.idPaciente = idPaciente
        inicial.esf = esf
        inicial.qtdComodos = qtdComodos
        inicial.aguaEncanada = aguaEncanada
        inicial.opinouDoencaCronica = opinouDoencaCronica
        inicial.opinouRemedio = opinouRemedio
        inicial.opinouEsf = opinouEsf
        inicial.pediuAuxilio = pediuAuxilio

        db = Database()
        db.saveData(inicial)
        self.atendimento.idInicial = db.selectData(inicial).id
        self.atendimento.primeiro = True

    #A partir daqui são os cadastros por sessões. Os parâmetros que não são requisitados ou
    #não precisam ser cadastrados são recebidos com um valor padrão None, pra esse valor
    #não precisar ser passado na função que chamará o Builder.
    def cadastrarDomicilio(self, moraSozinho, qtdPessoasDomicilio=None):
        self.atendimento.moraSozinho=moraSozinho
        self.atendimento.qtdPessoasDomicilio=qtdPessoasDomicilio
    
    def cadastrarVisitas(self, recebeuVisita, quemVisitou=None, porqueVisitou=None):
        self.atendimento.recebeuVisita=recebeuVisita
        self.atendimento.quemVisitou=quemVisitou
        self.atendimento.porqueVisitou=porqueVisitou
    
    def cadastrarIsolamento(self, consegueIsolamento, porqueMantemIsolamento=None, porqueNaoMantemIsolamento=None):
        self.atendimento.consegueIsolamento=consegueIsolamento
        self.atendimento.porqueMantemIsolamento=porqueMantemIsolamento
        self.atendimento.porqueNaoMantemIsolamento=porqueNaoMantemIsolamento
    
    def cadastrarQuarentena(self, consegueManter, qtdDias=None, apenasAtividadesEmergenciais=None):
        self.atendimento.consegueManter=consegueManter
        self.atendimento.qtdDias=qtdDias
        self.atendimento.apenasAtividadesEmergenciais = apenasAtividadesEmergenciais

    def cadastrarSintomas(self, grausFebre):
        self.atendimento.grausFebre=grausFebre
    
    def cadastrarOrientacoes(self, orientacoes):
        self.atendimento.orientacoes=orientacoes

    def finalizarAtendimento(self): #Cadastra o atendimento e o agendamento

        # Fazer isso ao fim
        #db = Database()
        #db.saveData(self.atendimento)
        #atendimento_id = db.selectData(self.atendimento)
        #Usar esse id para cadastrar o agendamento e todas as classes derivadas
        return
