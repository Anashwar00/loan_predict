import streamlit as st
from app import validate
from pydantic import ValidationError
import pandas as pd
import pickle

st.title("Loan-Approval-Prediction-")

with open('scalar_svm.pkl','rb') as f:
    scalar=pickle.load(f)
    
with open('grid_model.pkl','rb') as f:
    model=pickle.load(f)

no_of_dependents=st.selectbox('Enter no of dependents',
                              [0,1,2,3,4,5])

education=st.selectbox('Graduate or Not Graduate',['Graduate','Not Graduate'])

self_employed=st.selectbox("Are you self Emloyed ",['Yes','No'])

loan_term=st.text_input("Enter your loan in year")
cibil_score=st.text_input("Enter your cibil score")
residential_assets_value=st.text_input("Enter your residential_assets_value")
commercial_assets_value=st.text_input("Enter your commercial_assets_value")

if st.button('Submit'):
    try:
        loan_data=validate(
            no_of_dependents=no_of_dependents,
            education=education,
            self_employed=self_employed,
            loan_term=int(loan_term),
            cibil_score=float(cibil_score),
            residential_assets_value=float(residential_assets_value),
            commercial_assets_value=float(commercial_assets_value)
        )
        
        df=pd.DataFrame({
            'no_of_dependents':[loan_data.no_of_dependents],
            'education':[loan_data.education_numeric],
            'self_employed':[loan_data.employed_numeric],
            'loan_term':[loan_data.loan_term],
            'cibil_score':[loan_data.cibil_score],
            'residential_assets_value':[loan_data.residential_assets_value],
            'commercial_assets_value':[loan_data.commercial_assets_value]  
        })
        print("DataFrame sent to scaler:\n", df)
        X_test=scalar.transform(df)
        print("DataFrame sent to X_test:\n", X_test)
        X_test_sc=model.predict(X_test)[0]
        if X_test_sc==0:
            st.write('Rejected')
        else:
            st.write('Approved')
        
        
        
        
    
    except ValidationError as e:
        st.error("Validation Error!")
        st.json(e.errors())







