from fastapi import FastAPI
from app.core.config import settings
from app.utils.contracts_functions import get_contracts
from app.utils.json_formating import json_formating


app = FastAPI(title=settings.PROJECT_TITLE, version=settings.PROJECT_VERSION)


@app.get("/api/contracts")
def GET_contracts(category: str = "comunicacion_transporte", year: int = 2016):
    try:
        result = get_contracts(category,year)
        json = json_formating(result)
        return {"response": json}
    except Exception as e:
        print("An error ocurred", e)
