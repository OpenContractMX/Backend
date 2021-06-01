from fastapi import HTTPException
from app.utils.validate_trimester import validate_trimester
from app.utils.validate_month import validate_month
from app.utils.validate_year import validate_year
from app.utils.validate_category import validate_category


def general_contracts_validations(category: str, year: int, month: int, trimester: int):

    if month == None and trimester == None:

        if not validate_category(category):
            raise HTTPException(status_code=400, detail="Error category is not valid")

        if not validate_year(year):
            raise HTTPException(status_code=400, detail="Error year is not valid")

    elif month == None and not trimester == None:

        if not validate_category(category):
            raise HTTPException(status_code=400, detail="Error category is not valid")

        if not validate_year(year):
            raise HTTPException(status_code=400, detail="Error year is not valid")

        if not validate_trimester(trimester):
            raise HTTPException(status_code=400, detail="Error trimester is not valid")

    elif not month == None and trimester == None:

        if not validate_category(category):
            raise HTTPException(status_code=400, detail="Error category is not valid")

        if not validate_year(year):
            raise HTTPException(status_code=400, detail="Error year is not valid")

        if not validate_month(month):
            raise HTTPException(status_code=400, detail="Error month is not valid")

    else:
        raise HTTPException(status_code=400, detail="Error you can only send either month or trimester")
