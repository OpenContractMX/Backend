from app.db.connection import Database
from app.core.config import settings

db = Database(settings)


def get_contracts(category,year):
    query = f"""
    SELECT c.id, t.expedition_month, t.expedition_trimester, c.title, t.buyer_name, t.date, c.amount, c.currency, c.start_date, c.end_date 
    FROM {category} as t JOIN contracts as c ON t._id = c.entry_id
    WHERE t.expedition_year = {year}
    """
    db.connect()
    result = db.select_rows(query)
    return result
    # SELECT (c.id, c.currency, c.amount, c.start_date, c.end_date, t.MONTH, t.trimester, t.buyer_name) FROM contracts as c JOIN tags as t ON c.entry_id = t._id WHERE t.expedition_year = 2016
