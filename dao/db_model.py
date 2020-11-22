from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer
from sqlalchemy.dialects.postgresql import VARCHAR, DOUBLE_PRECISION

Base = declarative_base()

class ormCustomer(Base):
    __tablename__ = 'customers'

    Loan_ID = Column(Integer, primary_key=True)
    Gender = Column(VARCHAR, nullable=False)
    Married = Column(VARCHAR, nullable=False)
    Dependents = Column(VARCHAR, nullable=False)
    Education = Column(VARCHAR, nullable=False)
    Self_Employed = Column(VARCHAR, nullable=False)
    ApplicantIncome = Column(DOUBLE_PRECISION, nullable=False)
    CoapplicantIncome = Column(DOUBLE_PRECISION, nullable=False)
    LoanAmount = Column(DOUBLE_PRECISION, nullable=False)
    Loan_Amount_Term = Column(DOUBLE_PRECISION, nullable=False)
    Credit_History = Column(DOUBLE_PRECISION, nullable=False)
    Property_Area = Column(VARCHAR, nullable=False)
    Loan_Status = Column(VARCHAR, nullable=False)
