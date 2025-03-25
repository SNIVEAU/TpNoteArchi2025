from sqlalchemy.sql.expression import func
tasks = [
{
"id": 1 ,
"title": " Courses " ,
"description": " Salade , Oignons , Pommes , Clementines " ,
"done": True
} ,
{
"id": 2 ,
"title": " Apprendre REST " ,
"description": " Apprendre mon cours et comprendre les exemples " ,
"done": False
} ,
{
"id": 3 ,
"title": " Apprendre Ajax " ,
"description": " Revoir les exemples et ecrire un client REST JS avec Ajax " ,
"done": False
}
]
from .app import db
import sqlite3
from flask import jsonify
class Questionnaire(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))

    def __init__(self, name,id):
        self.name = name
        self.id = id
    def set_name(self,nom):
        self.name = nom
    def __repr__(self):
        return "<Questionnaire (%d) %s>" % (self.id, self.name)

    def to_json(self):
        
        json = {
            'id': self.id,
            'name': self.name,
            'questions': []
        }
        questions = Question.query.filter(Question.questionnaire_id == self.id).all()
        for question in questions:
            json['questions'].append(question.to_json())
        return json
    

class Question(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120))
    questionType = db.Column(db.String(120))
    questionnaire_id = db.Column(db.Integer, db.ForeignKey('questionnaire.id'))
    questionnaire = db.relationship("Questionnaire", backref=db.backref("questions", lazy="dynamic"))

    def __init__(self,id,title,questionType,questionnaire_id):
        self.id = id
        self.title =title
        self.questionType = questionType
        self.questionnaire_id = questionnaire_id
    def to_json(self):
        json = {
            'id': self.id,
            'title': self.title,
            'questionType': self.questionType,
            'questionnaire_id':self.questionnaire_id,
        }
        return json
    

def getall_questions():
    questions = Question.query.all()
    res = []
    for q in questions:
        res.append(q.to_json())
    return res
def getall_questionnaires():
    questionnaires = Questionnaire.query.all()
    res = []
    for q in questionnaires:
        res.append(q.to_json())
    return res
def inserer_questionnaire(name):
    max_id = db.session.query(func.max(Questionnaire.id)).scalar()
    id = (max_id or 0) + 1
    questionnaire = Questionnaire(name,id)
    db.session.add(questionnaire)
    db.session.commit()
    return questionnaire
def get_max_idquestion():
    max_id = db.session.query(func.max(Question.id)).scalar()
    return (max_id or 0) + 1
def inserer_question(title,questionType,questionnaire_id):
    id = get_max_idquestion()
    question = Question(id,title,questionType,questionnaire_id)
    db.session.add(question)
    db.session.commit()
    return question

def get_question_by_id_question(id):
    question = Question.query.filter(Question.id == id).first()
    if question is None:
        return None
    return question

def get_questionnaire_by_id(id):
    questionnaire = Questionnaire.query.filter(Questionnaire.id == id).first()
    if questionnaire is None:
        return None
    return questionnaire

def get_question_by_questionnaire_id(id):
    questions = Question.query.filter(Question.questionnaire_id == id).all()
    if questions is None:
        return None
    return questions