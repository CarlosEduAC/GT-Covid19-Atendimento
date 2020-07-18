from .sections import *

""" class Fieldset():
    def __init__(self, name, sections):
        self.name = name
        self.sections = sections
    
    def preencherPaciente(self, paciente):
        self.sections[0].inserirInfoPaciente(paciente) """


def preencherPaciente(fieldset, paciente):
    fieldset["sections"][0] = inserirInfoPaciente(fieldset["sections"][0], paciente)
    return fieldset

""" fieldsetConjuntoUsuario = Fieldset(
    name="Dados Pessoais",
    sections=[
        informacoesBasicasPreenchidas
    ]
) """

fieldsetConjunto0 = {
    "name": "Dados pessoais",
    "sections": [
        informacoesBasicas,
    ],
}

fieldsetConjunto1 = {
    "name": "Tentativa",
    "sections": [
        tentativa,
    ],
}

fieldsetConjunto2 = {
    "name": "Dados sobre saúde",
    "sections": [
        doencasCronicas,
        esfReferencia,
    ],
}

fieldsetConjunto3 = {
    "name": "Dados sociais",
    "sections": [
        caracteristicasDomicilioAuxilio,
    ],
}

fieldsetConjunto4 = {
    "name": "Isolamento domiciliar",
    "sections": [
        domicilio,
        visitas,
        isolamentoDomiciliar,
    ],
}

fieldsetConjunto5 = {
    "name": "Sintomas COVID",
    "sections": [
        sintomascovid,
    ],
}

fieldsetConjunto6 = {
    "name": "Encerramento",
    "sections": [
        orientacoesfinais
    ],
}
