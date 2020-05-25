# GT-Covid19-Atendimento
Sistema web responsável pelo atendimento de pacientes com suspeitas de coronavírus.

# Passo a passo para iniciar projeto
. Necessário ter o Python 3.x instalado na máquina
. Necessário ter o GIT instalado na máquina

- Clonando o projeto

    git clone https://github.com/CarlosEduAC/GT-Covid19-Atendimento.git

- Instalando dependências 

    pip install -r requirements.txt

- Iniciando o sistema

    python app/app.py

# Passo a passo para o versionamento do projeto

- Entrar no link do projeto 
    
    https://github.com/CarlosEduAC/GT-Covid19-Atendimento

- Fazer o Fork do projeto

- Clonar o projeto para uma pasta

    git clone "Link do projeto forkado no seu github'

- Atualizando o projeto (local) *

    git add .
    git commit -m "- Exemplo de Commit"
    git pull

- Atualizando o projeto (git)

    git push

- Abrir a pagina do seu fork e clicar em :
    
    New pull request

- Ao começar uma nova feature ou tarefa , atualize seu repositorio local com as atualizações do Git principal do projeto :

    git chekout master 
    git fetch upstream 
    git merge upstream/master

     git add .
    git commit -m "- Exemplo de Commit"
    git pull


* é aconselhável criar um novo branch a cada nova 'feature'.
    
    git checkout -b NomeDoNovoBranch
