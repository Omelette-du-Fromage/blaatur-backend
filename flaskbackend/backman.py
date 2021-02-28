import flask
from flask import jsonify

app = flask.Flask(__name__)
app.config["DEBUG"] = True

@app.route('/', methods=['GET'])
def home():
    return "<h1>Distant Reading Archive</h1><p>This site is a prototype API for distant reading of science fiction novels.</p>"

@app.route('/testing', methods=['GET'])
def data():
    json_return = [{"start":"Voss", "end": "Bergen"}]
    return jsonify(json_return)

app.run()