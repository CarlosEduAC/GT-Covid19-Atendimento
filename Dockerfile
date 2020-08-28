# Instala o ambiente a partir de uma imagem Debian, SO do servidor na UFRJ Macae
# Rodando esta imagem: docker run -t -i -p 0.0.0.0:5000:5000 f5a375a812f1

FROM debian
LABEL Description="Esta imagem é usada para instalar e rodar o Sistema de Telemonitoramento da Covid-19"

# Define 'code' como diretório de trabalho no contêiner
WORKDIR /code

# Atualiza instaladores
RUN apt update
RUN apt-get update

# Instala o PIP
RUN apt install --yes python3-pip

COPY requirements.txt requirements.txt

# Instala os requisitos do sistema
RUN pip3 install -r requirements.txt

# Instala bibliotecas para visualizacao de PDF
RUN apt-get install --yes libcairo2 libpango-1.0-0 libpangocairo-1.0-0 libgdk-pixbuf2.0-0 libffi-dev

COPY app .

EXPOSE 5000

COPY populatedb_runapp.sh populatedb_runapp.sh
RUN ["chmod", "+x", "populatedb_runapp.sh"]
ENTRYPOINT ["env", "USER_DOCKER_TELEMONITORAMENTO=root", "PASS_DOCKER_TELEMONITORAMENTO=123456", "BD_DOCKER_TELEMONITORAMENTO=bd", "./populatedb_runapp.sh"]
