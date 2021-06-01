from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware
from app.core.config import settings

from app.utils.contracts_functions import get_contracts, get_download_year
from app.utils.contracts_functions import get_contracts_month, get_download_month
from app.utils.contracts_functions import (
    get_contracts_trimester,
    get_download_trimester,
)

from app.utils.json_formating import json_formating_year
from app.utils.json_formating import json_formating_month_trimester

from app.utils.validate_category import validate_category
from app.utils.validate_year import validate_year
from app.utils.validate_month import validate_month
from app.utils.validate_trimester import validate_trimester

from app.utils.convert_to_csv import convert_to_csv

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
async def GET_contracts(
    category: str = "",
    year: int = 0,
    month: int = 0,
    trimester: int = 0,
):

    if not validate_category(category):
        raise HTTPException(status_code=400, detail="Error category is not valid")
        # return {"response": "Error categorynv is not valid"}

    if not validate_year(year):
        raise HTTPException(status_code=400, detail="Error year is not valid")

    if not validate_month(month):
        raise HTTPException(status_code=400, detail="Error month is not valid")

    if not validate_trimester(trimester):
        raise HTTPException(status_code=400, detail="Error trimester is not valid")

    if (month > 0) & (trimester > 0):
        raise HTTPException(
            status_code=400,
            detail="Error you can only filter by month or trimester but not both",
        )

    if month > 0:
        try:
            result = get_contracts_month(category, year, month)
            json = json_formating_month_trimester(result)
        except Exception as e:
            print("error formatting in month json", e)
            raise HTTPException(
                status_code=500,
                detail="Internal Error",
            )

    elif trimester > 0:
        try:
            result = get_contracts_trimester(category, year, trimester)
            json = json_formating_month_trimester(result)
        except Exception as e:
            print("error formatting in trimester json", e)
            raise HTTPException(
                status_code=500,
                detail="Internal Error",
            )

    else:
        try:
            result = get_contracts(category, year)
            json = json_formating_year(result)
        except Exception as e:
            print("error formatting in year json", e)
            raise HTTPException(
                status_code=500,
                detail="Internal Error",
            )

    return {"response": json}


@app.get("/api/download")
def GET_contracts_csv(
    category: str = "",
    year: int = 0,
    month: int = 0,
    trimester: int = 0,
):
    try:

        if not validate_category(category):
            return {"response": "Error category is not valid"}

        if not validate_year(year):
            return {"response": "Error year is not valid"}

        if not validate_month(month):
            return {"response": "Error month is not valid"}

        if not validate_trimester(trimester):
            return {"response": "Error trimester is not valid"}

        if (month > 0) & (trimester > 0):
            return {
                "response": "Error you can only filter by month or trimester but not both"
            }

        if month > 0:
            result = get_download_month(category, year, month)
            convert_to_csv(result)
            filename = f"{category}_{year}_Month_{month}.csv"
        elif trimester > 0:
            result = get_download_trimester(category, year, trimester)
            convert_to_csv(result)
            filename = f"{category}_{year}_Quarter_{trimester}.csv"
        else:
            result = get_download_year(category, year)
            convert_to_csv(result)
            filename = f"{category}_{year}.csv"
        # print("si estamos llegando")
        return FileResponse(
            path="download.csv",
            media_type="text/csv",
            filename=filename,
            headers={"Content-Type": "text/csv"},
        )

    except Exception as e:
        print(f"An error ocurred: {e}")
