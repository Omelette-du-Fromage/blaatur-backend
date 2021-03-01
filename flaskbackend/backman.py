import flask
from flask import jsonify
from flask_cors import CORS, cross_origin

app = flask.Flask(__name__)
app.config["DEBUG"] = True

#cors = CORS(app)
#app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/', methods=['GET'])
def home():
    return "<h1>Distant Reading Archive</h1><p>This site is a prototype API for distant reading of science fiction novels.</p>"

@cross_origin(supports_credentials = True)
@app.route('/testing', methods=['GET'])
def data():
    json_return = [{"start":"Voss", "end": "Bergen"}]
    return jsonify(json_return)