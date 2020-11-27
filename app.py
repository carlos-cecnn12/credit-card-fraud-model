from flask import Flask,request,jsonify
import numpy as np
import joblib

app=Flask(__name__)

@app.route('/')
def index():
 return 'Model Service Up!'

def ValuePredictor(to_predict_list):
 to_predict = np.array(to_predict_list).reshape(1,-1)
 loaded_model = joblib.load("model1.joblib")
 result = loaded_model.predict(to_predict)
 return result[0]

@app.route('/predict',methods = ['POST'])
def result():
 if request.method == 'POST':
    to_predict_list = request.json
    to_predict_list=list(to_predict_list.values())
    res = "fraud" if ValuePredictor(to_predict_list) else "no_fraud"
    return jsonify({'prediction':res})

if __name__ == "__main__":
 app.run(debug=True)