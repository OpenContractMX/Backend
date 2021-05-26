from fastapi import FastAPI, Depends
from core.config import settings
from db.session import engine
from db.base_class import Base
from sqlalchemy.orm import Session

from db.session import get_db
from db.models import contracts, dependencies


# Creating the tables describe on models
# def create_tables():
#     Base.metadata.create_all(bind=engine)


def start_application():
    app = FastAPI(title=settings.PROJECT_TITLE, version=settings.PROJECT_VERSION)
    # create_tables()
    return app


app = start_application()


def get_contracts(db: Session, year: int, limit: int = 5):
    return db.query(contracts.Contracts).join(dependencies.Dependencies).filter(
        dependencies.Dependencies.expedition_year == 2016).limit(limit).all()
    # SELECT (c.id, c.currency, c.amount, c.start_date, c.end_date, t.MONTH, t.trimester, t.buyer_name) FROM contracts as c JOIN tags as t ON c.entry_id = t._id WHERE t.expedition_year = 2016


@app.get('/')
def hello_api(db: Session = Depends(get_db)):
    try:
        contratos_test = get_contracts(db, 0, 1)
        print(contratos_test[0])
    except Exception as e:
        print('An error ocurred', e)
    return {'hello': 'world'}
