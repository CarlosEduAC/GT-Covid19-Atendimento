#!/bin/bash
echo 'Rodando ALEMBIC'
alembic upgrade head
echo 'Disparando APP'
python3 app.py dev docker
