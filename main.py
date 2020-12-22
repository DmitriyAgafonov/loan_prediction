import os
import numpy as np
import pandas as pd
import pickle


from flask import Flask, redirect, url_for, request, session, render_template, flash
from flask_restful import Resource, Api
#from forms.forms import SignUpForm

from dao.db_connection import PostgreDb
from dao.db_model import *
from forms.forms import UserInputForm

#import plotly
#import plotly.graph_objs as go
#import json

app = Flask(__name__)
app.secret_key = 'development-key'
api = Api(app)
db = PostgreDb()

def FittingData(user_data):
    with open('fitted_data.pkl', 'rb') as f:
        fitted_ohe_loaded, logreg_clf_loaded = pickle.load(f)
    cols = ['Dependents', 'ApplicantIncome', 'CoapplicantIncome', 'LoanAmount', 'Loan_Amount_Term', 'Property_Area',
            'Gender_Male', 'Married_Yes', 'Education_Not Graduate', 'Self_Employed_Yes', 'Credit_History_1.0',
            'Loan_Status_Y']
    vals = [[user_data['dependents'],
             int(user_data['applicant_income']),
             float(user_data['coapplicant_income']),
             float(user_data['loan_amount']),
             float(user_data['loan_amount_term']),
             user_data['property_area'],
             1 if user_data['gender'] == 'Male' else 0,
             1 if user_data['married'] == 'Yes' else 0,
             0 if user_data['education'] == 'Graduate' else 1,
             1 if user_data['self_employed'] == 'Yes' else 0,
             int(user_data['credit_history']),
             'plug']]
    sample = pd.DataFrame(vals, columns=cols)
    sample_tomodel = fitted_ohe_loaded.transform(sample)[0][:-1].reshape(1, -1)
    thresh = 0.55
    y_pred_test_thresh = logreg_clf_loaded.predict_proba(sample_tomodel)[:, 1]
    y_pred = (y_pred_test_thresh > thresh).astype(int)
    return y_pred[0]

@app.route("/", methods = ['GET'])
def root():
    return render_template('index.html')
    
@app.route('/registration', methods=["GET", "POST"])
def register():
    form = UserInputForm()
    if form.validate_on_submit():
        to_predict_list = request.form.to_dict()
        loan_status_result = FittingData(to_predict_list)
        if int(loan_status_result) == 1:
            loan_status_result = 'Yes'
            prediction = 'Loan is approved'
            flash(f'Your prediction: {prediction}', 'success')
        else:
            loan_status_result = 'No'
            prediction = 'Loan is not approved'
            flash(f'Your prediction: {prediction}', 'danger')

        customer = ormCustomer(gender=form.gender.data,
                               married=form.married.data,
                               dependents=form.dependents.data,
                               education=form.education.data,
                               self_employed=form.self_employed.data,
                               applicantincome=form.applicant_income.data,
                               coapplicantincome=form.coapplicant_income.data,
                               loanamount=form.loan_amount.data,
                               loan_amount_term=form.loan_amount_term.data,
                               credit_history=form.credit_history.data,
                               property_area=form.property_area.data,
                               loan_status=loan_status_result)
        db.sqlalchemy_session.add(customer)
        db.sqlalchemy_session.commit()
        return redirect(url_for('root'))
    return render_template('registration.html', form=form)

@app.route('/customers', methods=['GET', 'POST'])
def customer_table():
    result = db.sqlalchemy_session.query(ormCustomer).all()
    return render_template('customers.html', customers=result)

if __name__ == "__main__":
        app.run(host='0.0.0.0', debug=True, threaded=True)