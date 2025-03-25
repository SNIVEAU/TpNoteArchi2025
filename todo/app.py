from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
from flask import Flask
from flask_cors import CORS

def mkpath(path):
	return os.path.abspath(path)

app = Flask ( __name__ )
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+mkpath("../myapp.db")
db = SQLAlchemy(app)
cors = CORS(app, resources={r"/todo/api/v1.0/*": {"origins": "*"}})
