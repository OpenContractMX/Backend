from fastapi import FastAPI, Depends
from core.config import settings
from db.session import engine
from db.base_class import Base
from sqlalchemy.orm import Session

from db.session import get_db
from db.models import model
from sqlalchemy import text

def start_application():
    app = FastAPI(title=settings.PROJECT_TITLE, version=settings.PROJECT_VERSION)
    return app


app = start_application()


def get_contracts(db: Session, year: int, limit: int = 5,dependency_name: str=None ):
    sql = text("SELECT comunicacion_transporte.expedition_year AS comunicacion_transporte_expedition_year, contracts.title AS contracts_title FROM comunicacion_transporte JOIN contracts ON comunicacion_transporte._id = contracts.entry_id WHERE comunicacion_transporte.expedition_year = 2016 LIMIT 5")
    result  = db.execute(sql)
    names = [row[0] for row in result]
    #info = db.query(model.ComunicacionTransporte.expedition_year,model.Contracts.title).join(model.Contracts).filter(model.ComunicacionTransporte.expedition_year == 2016).limit(limit)
    return names
    # SELECT (c.id, c.currency, c.amount, c.start_date, c.end_date, t.MONTH, t.trimester, t.buyer_name) FROM contracts as c JOIN tags as t ON c.entry_id = t._id WHERE t.expedition_year = 2016


@app.get('/')
def hello_api(db: Session = Depends(get_db)):
    try:
        contratos_test = get_contracts(db, 0, 5,"comunicacion_transporte")
        return {'title': contratos_test}
    except Exception as e:
        print('An error ocurred', e)
    
    
