from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.core.config import settings

from app.utils.contracts_functions import get_contracts
from app.utils.contracts_functions import get_contracts_month
from app.utils.contracts_functions import get_contracts_trimester

from app.utils.json_formating import json_formating_year
from app.utils.json_formating import json_formating_month_trimester

from app.utils.validate_category import validate_category
from app.utils.validate_year import validate_year

app = FastAPI(title=settings.PROJECT_TITLE, version=settings.PROJECT_VERSION)

origins = [
    "http://localhost",
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/api/contracts")
def GET_contracts(category: str = "comunicacion_transporte", year: int = 2016, month: int = 0, trimester: int = 0 ):
    try:

        if not validate_category(category):
            return {"response": "Error category is not valid"} 

        if not validate_year(year):
            return {"response": "Error year is not valid"}

        if (month > 0) & (trimester > 0):
            return {"response": "Error you can only filter by month or trimester but not both"}

        if month > 0:
            result = get_contracts_month(category,year,month)
            json = json_formating_month_trimester(result)

        elif trimester > 0:
            result = get_contracts_trimester(category,year,trimester)
            json = json_formating_month_trimester(result)

        else:
            result = get_contracts(category,year)
            json = json_formating_year(result)
            
        return {"response": json}
    except Exception as e:
        print("An error ocurred", e)


@app.get("/api/download")
def GET_contracts(category: str = "comunicacion_transporte", year: int = 2016, month: int=None, trimester: int=None):
    try:

        if not validate_category(category):
            return {"response": "Error category is not valid"} 

        if not validate_year(year):
            return {"response": "Error year is not valid"}

        

        return {"response": "xd"}
    except Exception as e:
        print("An error ocurred", e)
