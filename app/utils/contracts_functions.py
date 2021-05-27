from app.db.connection import Database
from app.core.config import settings

db = Database(settings)


def get_contracts():
    query = "SELECT comunicacion_transporte.expedition_year AS comunicacion_transporte_expedition_year, contracts.title AS contracts_title FROM comunicacion_transporte JOIN contracts ON comunicacion_transporte._id = contracts.entry_id WHERE comunicacion_transporte.expedition_year = 2016 LIMIT 5"
    db.connect()
    result = db.select_rows(query)
    print(result)
    return result
    # SELECT (c.id, c.currency, c.amount, c.start_date, c.end_date, t.MONTH, t.trimester, t.buyer_name) FROM contracts as c JOIN tags as t ON c.entry_id = t._id WHERE t.expedition_year = 2016
