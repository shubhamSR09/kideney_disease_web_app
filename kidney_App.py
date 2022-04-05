from flask import Flask, render_template, request
import pickle
import numpy as np



filename = 'kideny.pkl'
lr = pickle.load(open(filename, 'rb'))

app = Flask(__name__)

@app.route('/')
def home():
	return render_template('kideny.html')

@app.route('/predict', methods=['POST'])
def predict():
    my_prediction=''
    if request.method == 'POST':
        age = int(request.form['age'])
        bp = int(request.form['bp'])
        al = int(request.form['al'])
        pcc = int(request.form['pcc'])
        bgr = int(request.form['bgr'])
        bu = int(request.form['bu'])
        sc = int(request.form['sc'])
        hemo = int(request.form['hemo'])
        pcv = int(request.form['pcv'])
        htn = int(request.form['htn'])
        dm = int(request.form['dm'])
        appet = int(request.form['appet'])
        
        
        data = np.array([[age, bp, al, pcc, bgr, bu, sc, hemo, pcv, htn, dm, appet]])
        my_prediction = lr.predict(data)
        
        
        return render_template('kideny_result.html', prediction=my_prediction)

if __name__ == '__main__':
	app.run(debug=True)