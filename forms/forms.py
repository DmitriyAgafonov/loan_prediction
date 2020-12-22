from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, HiddenField, SelectField, BooleanField
from wtforms.validators import DataRequired, Regexp

class SignUpForm(FlaskForm):

    loan_id = HiddenField()

    gender = SelectField("Gender: ",
                         choices=[('Male', 'Male'), ('Female', 'Female')],
                         validators=[DataRequired("Please enter your gender.")])

    married = SelectField("Married: ",
                          choices=[('Yes', 'Yes'), ('No', 'No')],
                          validators=[DataRequired("Please enter your marriage status.")])

    dependents = SelectField("Dependents: ",
                            choices=[('0', '0'), ('1', '1'), ('2', '2'), ('3+', '3+')],
                            validators=[DataRequired("Please enter your dependents.")])

    education = SelectField("Education: ",
                            choices=[('Graduate', 'Graduate'), ('Not Graduate', 'Not Graduate')],
                            validators=[DataRequired("Please enter your graduation status.")])

    self_employed = SelectField("Self employment: ",
                                choices=[('Yes', 'Yes'), ('No', 'No')],
                                validators=[DataRequired("Please enter your employment status.")])

    applicant_income = StringField("Applicant income: ",
                                   validators=[DataRequired("Please enter your applicant income."),
                                               Regexp("^[0-9]+$")])

    coapplicant_income = StringField("Co-applicant income: ",
                                     validators=[DataRequired("Please enter your co-applicant income."),
                                                 Regexp("^[0-9]+$")])

    loan_amount = StringField("Loan amount (in thousands): ",
                              validators=[DataRequired("Please enter your loan amount."),
                                          Regexp("^[0-9]+$")])

    loan_amount_term = StringField("Loan amount term (in months): ",
                                   validators=[DataRequired("Please enter your loan amount."),
                                               Regexp("^[0-9]+$")])

    credit_history = SelectField("Did you have loan before?: ",
                                 choices=[('1', 'Yes'), ('0', 'No')],
                                 validators=[DataRequired("Please enter your previous loan status.")])

    property_area = SelectField("Type of your property: ",
                                 choices=[('Urban', 'Urban'), ('Rural', 'Rural'), ('Semiurban', 'Semiurban')],
                                 validators=[DataRequired("Please enter type of your property.")])

    agreement = BooleanField("I agree to provide my personal data to our Service",
                             validators = [DataRequired("Please agree to continue.")])

    loan_status = HiddenField()

    submit = SubmitField("Submit")
