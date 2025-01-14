import pickle
from flask import Flask, jsonify , render_template, request
from sklearn.preprocessing import StandardScaler
import pandas as pd
import numpy as np


app = Flask(__name__)

ridge_model = pickle.load(open('ridge.pkl','rb'))
scaler = pickle.load(open('scaler.pkl','rb'))

@app.route("/")
def index():
    return render_template('index.html')

@app.route('/predictdata',methods=['GET','POST'])
def predict_datapoint():
    if request.method == 'POST':
        Temperature = float(request.form.get('Temperature'))
        RH = float(request.form.get('RH'))
        WS = float(request.form.get('WS'))
        Rain = float(request.form.get('Rain'))
        FFMC = float(request.form.get('FFMC'))
        DMC = float(request.form.get('DMC'))
        ISI = float(request.form.get('ISI'))
        Classes = float(request.form.get('Classes'))
        Region = float(request.form.get('Region'))

        input_data = scaler.transform([[Temperature,RH,WS,Rain,FFMC,DMC,7.6,ISI,Classes,Region]])
        result = ridge_model.predict(input_data)

        return render_template('home.html', result = result[0])
        
    else:
        return render_template('home.html')


if __name__== "__main__":
    app.run()