from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.core.config import settings
from app.utils.contracts_functions import get_contracts
from app.utils.json_formating import json_formating
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
def GET_contracts(category: str = "comunicacion_transporte", year: int = 2016):
    try:

        if not validate_category(category):
            return {"response": "Error category is not valid"} 

        if not validate_year(year):
            return {"response": "Error year is not valid"}

        result = get_contracts(category,year)
        json = json_formating(result)
        return {"response": json}
    except Exception as e:
        print("An error ocurred", e)
