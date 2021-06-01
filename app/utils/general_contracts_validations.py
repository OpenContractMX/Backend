from fastapi import HTTPException
from app.utils.validate_trimester import validate_trimester
from app.utils.validate_month import validate_month
from app.utils.validate_year import validate_year
from app.utils.validate_category import validate_category


def general_contracts_validations(category: str, year: int, month: int, trimester: int):
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
