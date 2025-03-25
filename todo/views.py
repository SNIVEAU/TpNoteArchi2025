from flask import jsonify , abort , make_response , request, url_for
from . app import app
from . models import *
def make_public_task ( task ) :
    new_task = {}
    for field in task :
        print(field)
        if field == 'id':
            new_task["uri"] = url_for ("get_task",task_id = task ["id"] ,_external = True )
        else :
            new_task [field] = task [field]
    # print(new_task["description"])
    return new_task
@app.route("/todo/api/v1.0/tasks" , methods = ["GET"])
def get_tasks () :
    return jsonify ( tasks =[ make_public_task (t) for t in tasks ])

@app.route("/todo/api/v1.0/tasks/<int:task_id>", methods = ["GET"])
def get_task(task_id):
    for task in tasks:
        if task['id'] ==task_id:
            return jsonify ({"task": make_public_task(task)})


@app.route ("/todo/api/v1.0/tasks",methods = ["POST"])
def create_task () :
    if not request.json or not "title" in request.json :
        abort (400)
    task = {
    "id": tasks[-1]["id"] + 1,
    "title": request.json["title"] ,
    "description": request.json.get("description","") ,
    "done": False
    }
    tasks.append (task)
    return jsonify ({"task": make_public_task(task)}),201

@app . errorhandler (404)
def not_found ( error ) :
    return make_response(jsonify({" error ": " Not found "}),404)

@app . errorhandler (400)
def not_found ( error ) :
    return make_response (jsonify({"error":"Bad request"}),400)

@app.route('/todo/api/v1.0/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    task = [task for task in tasks if task['id'] == task_id]
    if len(task) == 0:
        abort(404)
    if not request.json:
        abort(400)
    if 'title' in request.json and type(request.json['title']) != str:
        abort(400)
    if 'description' in request.json and type(request.json['description']) is not str:
        abort(400)
    if 'done' in request.json and type(request.json['done']) is not bool:
        abort(400)
    task[0]['title'] = request.json.get('title', task[0]['title'])
    task[0]['description'] = request.json.get('description', task[0]['description'])
    task[0]['done'] = request.json.get('done', task[0]['done'])
    return jsonify({'task': make_public_task(task[0])})

@app.route('/todo/api/v1.0/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    task = [task for task in tasks if task['id'] == task_id]
    if len(task) == 0:
        abort(404)
    tasks.remove(task[0])
    return jsonify({'result': True})

# @app.route("/todo/api/v1.0/questionnaires", methods=["POST"])
# def create_questionnaire():
#     if not request.json or not "name" in request.json or not "id" in request.json:
#         abort(400)
#     questionnaire = inserer_questionnaire(request.json["name"], request.json["id"])

#     return jsonify({"questionnaire": questionnaire.to_json()}), 201

@app.route("/todo/api/v1.0/questionnaires", methods=["POST"])
def create_questionnaire():
    if not request.json or not "name" in request.json:
        abort(400)
    questionnaire = inserer_questionnaire(request.json["name"])

    return jsonify({"questionnaire": questionnaire.to_json()}), 201

@app.route("/todo/api/v1.0/questionnaires", methods=["GET"])
def get_questionnaires():
    questionnaires = getall_questionnaires()
    return jsonify({"questionnaires": questionnaires})

@app.route("/todo/api/v1.0/questions",methods=["GET"])
def get_questions():
    questions = getall_questions()
    return jsonify({"question": questions})


@app.route("/todo/api/v1.0/questions/<int:id>",methods=["GET"])
def get_question(id):
    question = get_question_by_id_question(id)
    if not question:
        abort(404)
    return jsonify({"question": question.to_json()})

@app.route("/todo/api/v1.0/questionnaires/<int:id>",methods=["GET"])
def get_questionnaire(id):
    questionnaire = get_questionnaire_by_id(id)
    if not questionnaire:
        abort(404)
    return jsonify({"questionnaire": questionnaire.to_json()})

@app.route("/todo/api/v1.0/questions",methods=["POST"])
def creer_questions():
    if not request.json or not "title" in request.json or not "questionType" in request.json or not "questionnaire_id" in request.json:
        abort(400)
    # if db.session.query(Questionnaire).filter(Questionnaire.id == request.json["questionnaire_id"]).count() != 0:
    #     abort(404)
    question = inserer_question(request.json["title"], request.json["questionType"], request.json["questionnaire_id"])
    return jsonify({"questions":question.to_json()})

@app.route("/todo/api/v1.0/questions/<int:id>",methods=["PUT"])
def modifier_question(id):
    if request.json:
        question = get_question_by_id_question(id)
        if not question:
            abort(404)
        for champ in request.json:
            if champ not in ["title", "questionType", "questionnaire_id"]:
                abort(400)
            if champ == "title":
                if type(request.json[champ]) != str:
                    abort(400)
                question.title = request.json["title"]
            if champ == "questionType":
                if type(request.json[champ]) != str:
                    abort(400)
                question.questionType = request.json["questionType"]
            if champ == "questionnaire_id":
                if type(request.json[champ]) != int:
                    abort(400)
                question.questionnaire_id = request.json["questionnaire_id"]

        db.session.commit()
        return jsonify({"question": question.to_json()})
    else:
        abort(400)
    
@app.route("/todo/api/v1.0/questionnaires/<int:id>",methods=["PUT"])
def modifier_questionnaire(id):
    if request.json:
        questionnaire = get_questionnaire_by_id(id)
        if not questionnaire:
            abort(404)
        for champ in request.json:
            if champ == "name":
                questionnaire.set_name(request.json["name"])

                if type(request.json[champ]) != str:
                    abort(400)
                print(questionnaire.name)

        db.session.commit()
        return jsonify({"questionnaire": questionnaire.to_json()})
    else:
        abort(400)



@app.route("/todo/api/v1.0/questionnaires/<int:id>", methods=["DELETE"])
def supprimer_questionnaire(id):
    ques = get_questionnaire_by_id(id)
    if not ques:
        abort(404)  
    questions = get_question_by_questionnaire_id(id)
    for question in questions:
        db.session.delete(question)
    db.session.delete(ques)
    db.session.commit()
    return jsonify({"result": "true"})

@app.route("/todo/api/v1.0/questions/<int:id>",methods=["DELETE"])
def supprimer_question(id):
    question = get_question_by_id_question(id)
    if not question:
        abort(404)
    db.session.delete(question)
    db.session.commit()
    return jsonify({"result":"true"})


            



        