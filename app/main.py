import flask
from flask import request, jsonify
from model.bert import find_answer

app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/', methods=['GET'])
def home():
    return "<h1>APIs</h1>"


@app.route('/api/v1/resources/answers', methods=['GET'])
def answer():
    if 'question' in request.args and 'context_term' in request.args:
        ques = str(request.args['question']).lower()
        wiki_term = str(request.args['context_term']).lower()
        answer_obj = find_answer(ques, wiki_term)
        return jsonify({"score":answer_obj["score"], "answer":answer_obj["answer"]})

    else:
        return "Error: No question or context term found. Please specify both."


app.run()
