from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, HiddenField, SelectField, BooleanField, PasswordField
from wtforms.validators import InputRequired, Regexp

class UserInputForm(FlaskForm):

    loan_id = HiddenField()

    gender = SelectField("Gender: ",
                         choices=[('Male', 'Male'), ('Female', 'Female')],
                         validators=[InputRequired("Please enter your gender.")])

    married = SelectField("Married: ",
                          choices=[('Yes', 'Yes'), ('No', 'No')],
                          validators=[InputRequired("Please enter your marriage status.")])

    dependents = SelectField("Dependents: ",
                            choices=[('0', '0'), ('1', '1'), ('2', '2'), ('3+', '3+')],
                            validators=[InputRequired("Please enter your dependents.")])

    education = SelectField("Education: ",
                            choices=[('Graduate', 'Graduate'), ('Not Graduate', 'Not Graduate')],
                            validators=[InputRequired("Please enter your graduation status.")])

    self_employed = SelectField("Self employment: ",
                                choices=[('Yes', 'Yes'), ('No', 'No')],
                                validators=[InputRequired("Please enter your employment status.")])

    applicant_income = StringField("Applicant income: ",
                                   validators=[InputRequired("Please enter your applicant income."),
                                               Regexp(regex='^\d+.*\d+$', message='Input decimal number')])

    coapplicant_income = StringField("Co-applicant income: ",
                                     validators=[InputRequired("Please enter your co-applicant income."),
                                                 Regexp(regex='^\d+.*\d+$', message='Input decimal number')])

    loan_amount = StringField("Loan amount (in thousands): ",
                              validators=[InputRequired("Please enter your loan amount."),
                                          Regexp(regex='^\d+.*\d+$', message='Input decimal number')])

    loan_amount_term = StringField("Loan amount term (in months): ",
                                   validators=[InputRequired("Please enter your loan amount."),
                                               Regexp("^\d+$")])

    credit_history = SelectField("Did you have loan before?: ",
                                 choices=[('1', 'Yes'), ('0', 'No')],
                                 validators=[InputRequired("Please enter your previous loan status.")])

    property_area = SelectField("Type of your property: ",
                                choices=[('Urban', 'Urban'), ('Rural', 'Rural'), ('Semiurban', 'Semiurban')],
                                validators=[InputRequired("Please enter type of your property.")])

    agreement = BooleanField("I agree to provide my personal data to our Service",
                             validators=[InputRequired("Please agree to continue.")])

    loan_status = HiddenField()

    submit = SubmitField("Submit")
