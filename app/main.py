from fastapi import FastAPI
from core.config import settings

from db.connection import connection

cursor = connection.cursor()


app = FastAPI(title=settings.PROJECT_TITLE, version=settings.PROJECT_VERSION)


def get_contracts():
    pass
    # SELECT (c.id, c.currency, c.amount, c.start_date, c.end_date, t.MONTH, t.trimester, t.buyer_name) FROM contracts as c JOIN tags as t ON c.entry_id = t._id WHERE t.expedition_year = 2016


@app.get("/")
def hello_api():
    try:
        cursor.execute(
            "SELECT comunicacion_transporte.expedition_year AS comunicacion_transporte_expedition_year, contracts.title AS contracts_title FROM comunicacion_transporte JOIN contracts ON comunicacion_transporte._id = contracts.entry_id WHERE comunicacion_transporte.expedition_year = 2016 LIMIT 5"
        )
        result = cursor.fetchall()
        print(result)
        cursor.close()
        return {"hi!": result}
    except Exception as e:
        print("An error ocurred", e)
