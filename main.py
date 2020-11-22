import os
import numpy as np
import pandas as pd
import pickle


from flask import Flask, redirect, url_for, request, session, render_template, flash
from forms.forms import SignUpForm

from dao.db_connection import PostgreDb
from dao.db_model import *
from forms.forms import SignUpForm


#from sqlalchemy import create_engine
#from sqlalchemy.orm import sessionmaker
#from sqlalchemy.sql import exists, extract, func, update
#from setup import user_database, todolist
#import plotly
#import plotly.graph_objs as go
#import json

app = Flask(__name__)
app.secret_key = 'development key'
db = PostgreDb()

def LoanPredictor(predict_list):
    to_predict = np.array(predict_list).reshape(1, 10)
    loaded_model = pickle.load(open("model.pkl", "rb"))
    result = loaded_model.predict(to_predict)
    return result[0]

@app.route("/", methods = ['GET'])
def root():
    return render_template('index.html')
    
@app.route('/registration', methods=["GET", "POST"])
def register():
    form = SignUpForm()
    if form.validate_on_submit():
        to_predict_list = request.form.to_dict()
        to_predict_list = list(to_predict_list.values())
        to_predict_list = list(map(int, to_predict_list))
        loan_status_result = LoanPredictor(to_predict_list)
        if int(loan_status_result) == 1:
            prediction = 'Loan is approved'
        else:
            prediction = 'Loan is not approved'
        customer = ormCustomer(Gender=form.gender.data,
                               Married=form.married.data,
                               Dependents=form.dependents.data,
                               Education=form.education.data,
                               Self_Employed=form.self_employed.data,
                               ApplicantIncome=form.applicant_income.data,
                               CoapplicantIncome=form.coapplicant_income.data,
                               LoanAmount=form.loan_amount.data,
                               Loan_Amount_Term=form.loan_amount_term.data,
                               Credit_History=form.credit_history.data,
                               Property_Area=form.property_area.data,
                               Loan_Status=loan_status_result)
        db.sqlalchemy_session.add_all([customer])
        db.sqlalchemy_session.commit()
        flash(f'Your prediction: {prediction}', 'success')
        return redirect(url_for('root'))
    return render_template('registration.html', form=form)

@app.route('/customers', methods=['GET', 'POST'])
def customer_table():
    result = db.sqlalchemy_session.query(ormCustomer).all()
    return render_template('customers.html', customers=result)

if __name__ == "__main__":
        app.run(debug=True, threaded=True)