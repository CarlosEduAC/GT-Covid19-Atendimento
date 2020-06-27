from controller.database import Database
from models.modelsDomainTable import Sexo, Raca

db = Database()


class Input:
    def type(self, type):
        self.type = type
        return self

    def name(self, name):
        self.name = name
        return self

    def label(self, label):
        self.label = label
        return self

    def placeholder(self, placeholder):
        self.placeholder = placeholder
        return self

    def required(self, required):
        self.required = required
        return self

    def mask(self, mask):
        self.mask = mask
        return self

    def options(self, options):
        self.options = options
        return self


nome = Input() \
    .type('text') \
    .name("nome") \
    .label("Nome completo") \
    .placeholder('Nome completo') \
    .required(True)

cpf = Input() \
    .type('text') \
    .name("cpf") \
    .label("CPF") \
    .required(True) \
    .mask("999.999.999-99") \
    .placeholder("999.999.999-99")

telefone = Input() \
    .type('text') \
    .name("telefone") \
    .label("Telefone") \
    .mask("(99) 99999999?9") \
    .placeholder("(99) 999999999")

nascimento = Input() \
    .type("date") \
    .name("nascimento") \
    .label("Data de nascimento")

sexo = Input() \
    .type("select") \
    .name("sexo") \
    .label("Sexo") \
    .required(True) \
    .options(db.selectAllData(Sexo))

raca = {
    "type": "select",
    "name": "raca",
    "label": "Raça",
    "required": True,
    "options": db.selectAllData(Raca)
}

endereco = {
    "name": "endereco",
    "label": "Endereço",
}
