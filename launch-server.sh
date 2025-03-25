#!/bin/bash

cd "$(dirname "$0")/serveur_questionnaire" || { echo "Directory not found"; exit 1; }
export FLASK_APP=app.py
export FLASK_ENV=development
flask run --debug