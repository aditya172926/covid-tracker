import matplotlib
matplotlib.use('Agg')
from flask import Flask, jsonify
from flask_cors import CORS

from functions_used import patient, weather_report
from sendtest import sendEmail
from india import graph

app = Flask(__name__)
CORS(app)

@app.route("/", methods = ['GET'])
def index():
    return jsonify('This is the integration of Flask and Angular. We have to make a covid 19 tracker')

@app.route("/weatherReport/", methods = ['GET'])
def WeatherReport():
    global weather
    weather = weather_report()
    return jsonify([weather])

@app.route("/patients/", methods = ['GET'])
def confirmed_patients():
    global a
    a = patient()
    return jsonify([a])

@app.route("/graphEmail/<email>", methods = ['GET', 'POST'])
def display_graph(email):
    graph()
    global x
    x = sendEmail(email)
    return jsonify(x)

if __name__ == '__main__':
    app.run(debug=True)