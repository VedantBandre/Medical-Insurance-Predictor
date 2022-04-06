import pickle
import numpy as np
import os
from flask import Flask, redirect, render_template, request, jsonify, url_for
THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
my_file = os.path.join(THIS_FOLDER, 'finalized_insurance_model.sav')
loaded_model = pickle.load(open(my_file, 'rb'))


app = Flask(__name__)
Flask.run(app)


# app-debug = True
@app.route("/")
def home():
    # return "<h1>Insurance Predictor</h1>"
    return render_template('index.html')
    

@app.route("/predict", methods=['GET'])
def prediction():
    parameters = request.args
    # output_list = []
    if request.method == 'GET':
        # age = int(request.form['age'])
        # sex_ = request.form['sex']
        # if sex_ == 'Male':
        #     sex = 0
        # if sex_ == 'Female':
        #     sex = 1
        # bmi = float(request.form['bmi'])
        # chi = int(request.form['chi'])
        # smo_ = request.form['smo']
        # if smo_ == 'Yes':
        #     smo = 0
        # if smo_ == 'No':
        #     smo = 1
        # reg_ = request.form['reg']
        # if reg_ == 'Southeast':
        #     reg = 0
        # if reg_ == 'Southwest':
        #     reg = 1
        # if reg_ == 'Northeast':
        #     reg = 2
        # if reg_ == 'Northwest':
        #     reg = 3
        
        
        age = int(parameters.get('age'))

        sex = str(parameters.get('sex'))
        # if sex_ == 'Male':
        #     sex = 0
        # if sex_ == 'Female':
        #     sex = 1

        bmi = float(parameters.get('bmi'))
        chi = int(parameters.get('chi'))
        
        smo = str(parameters.get('smo'))
        # if smo_ == 'Yes':
        #     smo = 0
        # if smo_ == 'No':
        #     smo = 1

        reg = str(parameters.get('reg'))
        # if reg_ == 'Southeast':
        #     reg = 0
        # if reg_ == 'Southwest':
        #     reg = 1
        # if reg_ == 'Northeast':
        #     reg = 2
        # if reg_ == 'Northwest':
        #     reg = 3
    
    # http://127.0.0.1/predict?age=20&sex=0&bmi=29&chi=0&smo=1&reg=2

    # changing input_data to a numpy array
    input_data = (age, sex, bmi, chi, smo, reg)
    input_data_as_numpy_array = np.asarray(input_data)

    # reshape the array
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)
    predictedVal = str(round(float(loaded_model.predict(input_data_reshaped)[0]),2))
    return render_template('result.html', result= predictedVal)
    print(predictedVal)
    # return redirect(url_for('results', res = predictedVal))

@app.route('/result/<float:result>')
def res():
    return render_template('result.html', res = {{ res }})

if __name__ == "__main__":
    app.run(host="0.0.0.0",port = 80, use_reloader=False, debug=False)
    