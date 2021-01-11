#!/bin/bash
export USER_DOCKER_TELEMONITORAMENTO=root
export PASS_DOCKER_TELEMONITORAMENTO=
export BD_DOCKER_TELEMONITORAMENTO=bd
echo 'Rodando ALEMBIC'
alembic upgrade head
echo 'Disparando APP'
python3 app.py dev docker
