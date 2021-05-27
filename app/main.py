from fastapi import FastAPI
from app.core.config import settings
from app.utils.contracts_functions import get_contracts


app = FastAPI(title=settings.PROJECT_TITLE, version=settings.PROJECT_VERSION)


@app.get("/api/contracts")
def GET_contracts():
    try:
        result = get_contracts()
        return {"hi!": result}
    except Exception as e:
        print("An error ocurred", e)
