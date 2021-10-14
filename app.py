# -*- coding: utf-8 -*-
"""
Created on Wed Oct 13 01:26:15 2021

@author: bamne
"""

from flask import Flask, render_template, request
from flask import jsonify
import requests
import pickle
import numpy as np
import sklearn
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import LabelEncoder


app = Flask(__name__)
clf = pickle.load(open('random_forest_classifier_placed_model.pkl', 'rb'))
scaled = pickle.load(open('scalers.pkl','rb'))



scaler = StandardScaler()
le = LabelEncoder()
@app.route("/predict", methods=['POST'])
def predict():
    if request.method == 'POST':
        gender_male=request.form['gender_male']
        if(gender_male == 'Female'):
            gender_male=1
        else:
            gender_male=0
        ssc_p=float(request.form['ssc_p'])
        ssc_b=request.form['ssc_b']
        if(ssc_b == 'Others'):
            ssc_b=1
        else:
            ssc_b=0
        hsc_p=float(request.form['hsc_p'])
        hsc_b=request.form['hsc_b']
        if(hsc_b == 'Others'):
            hsc_b=1
        else:
            hsc_b=0
        hsc_s=request.form['hsc_s']
        if(hsc_s == 'Commerce'):
            hsc_s=1
        elif(hsc_s == 'Science'):
            hsc_s=2
        else:
            hsc_s=0
        degree_p=float(request.form['degree_p'])
        degree_t=request.form['degree_t']
        if(degree_t == 'Comm&Mgmt'):
            degree_t=0
        elif(degree_t == 'Sci&Tech'):
            degree_t=2
        else:
            degree_t=1
        workex=request.form['workex']
        if(workex == 'No'):
            workex = 0
        else:
            workex = 1
        etest=float(request.form['etest'])
        specialisation=request.form['specialisation']
        if(specialisation == 'Mkt&HR'):
            specialisation=1
        else:
            specialisation=0
        mba_p=float(request.form['mba_p'])
       # for i in [gender_male,ssc_p,ssc_b,hsc_p,hsc_b,degree_p,degree_t,workex,etest,specialisation,mba_p]:
         #     i = scaler.fit_transform(np.array(i).reshape(1,-1)) 
        
        prediction=clf.predict(scaled.transform([[gender_male,ssc_p,ssc_b,hsc_p,degree_p,degree_t,workex,etest,specialisation,mba_p]]))
        if prediction == 0:
            return render_template('predict.html',prediction_text="Sorry you were not placed")
        else:
            return render_template('predict.html',prediction_text="Congratulations!!!")
    else:
        return render_template('predict.html')

if __name__=="__main__":
    app.run(debug=True)