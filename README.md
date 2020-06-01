# GT-Covid19-Atendimento
Sistema web responsável pelo atendimento de pacientes com suspeitas de coronavírus.

# Passo a passo para iniciar projeto
- Necessário ter o Python 3.8.3 instalado na máquina
- Necessário ter o GIT instalado na máquina

- Clonando o projeto

    - git clone https://github.com/CarlosEduAC/GT-Covid19-Atendimento.git

- Instalando dependências 

    - pip install -r requirements.txt

    - * Obs: A cada novo pacote necessario para a implmentação , lembrar de inclui-lo no requirements.txt. É melhor sobrar do que faltar ^^

- Iniciando o sistema

    - python app/app.py

# Passo a passo para o versionamento do projeto

- Entrar no link do projeto 
    
    https://github.com/CarlosEduAC/GT-Covid19-Atendimento

- Fazer o Fork do projeto

- Clonar o projeto para uma pasta

    - git clone "Link do projeto forkado no seu github'

- Atualizando o projeto (local) *

    - git add .
    - git commit -m "- Exemplo de Commit"
    - git pull

- Atualizando o projeto (git)

    - git push -f origin master

- Abrir a pagina do seu fork e clicar em :
    
    - New pull request

- Ao começar uma nova feature ou tarefa , atualize seu repositorio local com as atualizações do Git principal do projeto :

    *Apontar para o repositorio principal com o comando (*faça isso apenas uma vez*)
    - git remote add upstream https://github.com/CarlosEduAC/GT-Covid19-Atendimento


    - git checkout master 
    - git fetch upstream 
    - git rebase upstream/master


* é aconselhável, mas não obrigatório, criar um novo branch a cada nova 'feature'.
    
    - git checkout -b NomeDoNovoBranch
