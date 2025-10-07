from fastapi import FastAPI
from pydantic import BaseModel,Field,computed_field
from fastapi.responses import JSONResponse
import pickle
from typing import Dict,List

app=FastAPI()

# 	no_of_dependents	education	self_employed	loan_term	
# cibil_score	residential_assets_value	commercial_assets_value

class validate(BaseModel):
    no_of_dependents:int=Field(...,title="no of dependent out of 0,1,2,3,4,5",ge=0)
    education:str=Field(...,title='Graduate or Not Graduate')
    self_employed:str=Field(...,title="Yes/No")
    loan_term:int=Field(...,title="Loans in year")
    cibil_score:float=Field(...,title="add your cibil score")
    residential_assets_value:float=Field(...,title="Total residental_assets_value")
    commercial_assets_value:float=Field(...,title="Total commercial_assets_value")
    
    
    @computed_field
    @property
    def education_numeric(self)->int:
        return 1 if self.education=='Graduate' else 0
    
    @computed_field
    @property
    def employed_numeric(self)->int:
        return 1 if self.self_employed=='Yes' else 0
        
    
    
    
    

# @app.post("/predict")
# def predict(model:validate):
    