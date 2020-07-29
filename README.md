# GT-Covid19-Atendimento
Sistema web responsável pelo telemonitoramento de pacientes com suspeita de Covid-19.

# Passo a passo para iniciar o projeto
- Necessário ter o [Python 3](https://www.python.org/downloads/) instalado na máquina

- Necessário ter o [GIT](https://git-scm.com/downloads) instalado na máquina

- Necessário ter o [MySQL](https://www.mysql.com/) instalado na máquina (Devs novos sem acesso a VPN da UFRJ)
  
- Necessário ter o [WeasyPrint](https://weasyprint.readthedocs.io/en/latest/install.html) instalado para geração do PDF de agendamentos. Escolha o passo-a-passo para instalação do seu Sistema Operacional.

- Fazer o ![Fork](https://raw.githubusercontent.com/carlosbazilio/github-images/master/fork.png) do [projeto](https://github.com/CarlosEduAC/GT-Covid19-Atendimento) 

- Clonar o projeto do seu repositório para uma pasta local em sua máquina

    - git clone "Link do projeto forkado no seu github" (https://github.com/*seu-usuario-github*/GT-Covid19-Atendimento)

- Instalar dependências

    - **pip install -r requirements.txt**

    - * Obs: A cada novo pacote necessario para a implmentação , lembrar de incluí-lo no requirements.txt. É melhor sobrar do que faltar ^^

    - * Obs2: Se quiser, pode utilizar o recurso de [ambiente virtual](https://docs.python-guide.org/dev/virtualenvs/#lower-level-virtualenv) para evitar a instalação de pacotes de forma global em sua máquina

- Instalar o MySQL

    - Criar banco com nome 'covid3'

    - **python app/config_database.py dev** *(Cria o esquema no banco local com ORM)*

- Rodar o sistema

    - **python app/app.py dev** *(Acessa banco local)*
  
    - **python app/app.py teste** *(Acessa banco de dados de teste. Necessário ter VPN configurada)*
  
    - **python app/app.py** *(Acessa banco de dados de produção. Necessário ter VPN configurada)*

# Passo a passo para atualização do projeto

- Caso nunca tenha feito uma atualização, configure para seu repositório local apontar para o repositório principal (*faça isso apenas uma vez*)

    - **git remote add upstream** https://github.com/CarlosEduAC/GT-Covid19-Atendimento

    - **git checkout master** 

- Ao começar uma nova feature ou tarefa, atualize seu repositório local com as atualizações do Git principal do projeto:

    - **git fetch upstream** 

    - **git rebase upstream/master**

- Após codificar a alteração do projeto local, atualize o projeto no seu repositório forkeado:

    - **git add .**
    - **git commit -m "Exemplo de commit com comentário que descreva a atualização feita."**
    - **git push**

- Abrir a página *do seu fork* e clicar em:
    
    - ![New pull request](https://raw.githubusercontent.com/carlosbazilio/github-images/master/pr.png)

    - Comentar detalhando as informações sobre a atualização
