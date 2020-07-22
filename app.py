
import numpy as np
from flask import Flask, request, render_template
import pickle
import joblib
import random
import pandas as pd

app = Flask(__name__)
allow_pickle=False 
#loaded_model = pickle.load(open('finalized_model.sav', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

def ValuePredictor(to_predict_list):
    to_predict = np.array(to_predict_list).reshape(1, 6) 
    model = pickle.load(open('finalized_model.sav', "rb")) 
    result = model.predict(to_predict)
    #resultr= np.exp(result)
    return int(result[0]) 
  
@app.route('/predict',methods=['POST'])
def result():
    try:
        if request.method == 'POST':
            to_predict_list = request.form.to_dict()
            to_predict_list = list(to_predict_list.values()) 
            to_predict_list = list(map(int,to_predict_list))
            result = ValuePredictor(to_predict_list)            
            return render_template("index.html", prediction_text=' Production : kg {}/ha '.format(result))

    except:
        return render_template("index.html", prediction_text='Prediction Error !!!')
    
if __name__ == "__main__":
    app.run(debug=True)