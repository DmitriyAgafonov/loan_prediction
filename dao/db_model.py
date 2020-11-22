from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer
from sqlalchemy.dialects.postgresql import VARCHAR, DOUBLE_PRECISION

Base = declarative_base()

class ormCustomer(Base):
    __tablename__ = 'customers'

    loan_id = Column(Integer, primary_key=True)
    gender = Column(VARCHAR, nullable=False)
    married = Column(VARCHAR, nullable=False)
    dependents = Column(VARCHAR, nullable=False)
    education = Column(VARCHAR, nullable=False)
    self_employed = Column(VARCHAR, nullable=False)
    applicantincome = Column(DOUBLE_PRECISION, nullable=False)
    coapplicantincome = Column(DOUBLE_PRECISION, nullable=False)
    loanamount = Column(DOUBLE_PRECISION, nullable=False)
    loan_amount_term = Column(DOUBLE_PRECISION, nullable=False)
    credit_history = Column(DOUBLE_PRECISION, nullable=False)
    property_area = Column(VARCHAR, nullable=False)
    loan_status = Column(VARCHAR, nullable=False)
