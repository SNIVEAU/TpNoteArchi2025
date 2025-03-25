from .app import app, db
import sqlite3
from .models import Questionnaire, Question
from flask import jsonify, abort, make_response, request
from .models import *



@app.cli.command('initdb')
def initdb_command():
    db.create_all()
    