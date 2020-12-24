import pandas as pd
import pickle

class UserPrediction:
    def __init__(self, data):
        self.dependents = data['dependents']
        self.applicant_income = int(data['applicant_income'])
        self.coapplicant_income = float(data['coapplicant_income'])
        self.loan_amount = float(data['loan_amount'])
        self.loan_amount_term = float(data['loan_amount_term'])
        self.property_area = data['property_area']
        self.gender = 1 if data['gender'] == 'Male' else 0
        self.married = 1 if data['married'] == 'Yes' else 0
        self.education = 0 if data['education'] == 'Graduate' else 1
        self.self_employed = 1 if data['self_employed'] == 'Yes' else 0
        self.credit_history = int(data['credit_history'])

    def FittingData(self):
        with open('fitted_data.pkl', 'rb') as f:
            fitted_ohe_loaded, logreg_clf_loaded = pickle.load(f)
        cols = ['Dependents', 'ApplicantIncome', 'CoapplicantIncome', 'LoanAmount', 'Loan_Amount_Term', 'Property_Area',
                'Gender_Male', 'Married_Yes', 'Education_Not Graduate', 'Self_Employed_Yes', 'Credit_History_1.0',
                'Loan_Status_Y']
        vals = [[self.dependents,
                 self.applicant_income,
                 self.coapplicant_income,
                 self.loan_amount,
                 self.loan_amount_term,
                 self.property_area,
                 self.gender,
                 self.married,
                 self.education,
                 self.self_employed,
                 self.credit_history,
                 'plug']]
        sample = pd.DataFrame(vals, columns=cols)
        sample_to_model = fitted_ohe_loaded.transform(sample)[0][:-1].reshape(1, -1)
        thresh = 0.55
        y_pred_test_thresh = logreg_clf_loaded.predict_proba(sample_to_model)[:, 1]
        y_pred = (y_pred_test_thresh > thresh).astype(int)
        return y_pred[0]