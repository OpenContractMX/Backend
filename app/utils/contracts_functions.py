from app.db.connection import Database
from app.core.config import settings

db = Database(settings)


def get_contracts(category, year):
    query = f"""
    SELECT c.id, t.expedition_month, t.expedition_trimester, c.title, t.buyer_name, t.date, c.amount, c.currency, c.start_date, c.end_date 
    FROM {category} as t JOIN contracts as c ON t._id = c.entry_id
    WHERE t.expedition_year = {year}
    """
    db.connect()
    result = db.select_rows(query)
    return result
    # SELECT (c.id, c.currency, c.amount, c.start_date, c.end_date, t.MONTH, t.trimester, t.buyer_name) FROM contracts as c JOIN tags as t ON c.entry_id = t._id WHERE t.expedition_year = 2016


def get_contracts_month(category, year, month):
    query = f"""
    SELECT c.id, c.title, t.buyer_name, t.date, c.amount, c.currency
    FROM {category} as t JOIN contracts as c ON t._id = c.entry_id
    WHERE t.expedition_year = {year} and t.expedition_month = {month}
    """
    db.connect()
    result = db.select_rows(query)
    return result


def get_contracts_trimester(category, year, trimester):
    query = f"""
    SELECT c.id, c.title, t.buyer_name, t.date, c.amount, c.currency 
    FROM {category} as t JOIN contracts as c ON t._id = c.entry_id
    WHERE t.expedition_year = {year} and t.expedition_trimester = {trimester}
    """
    db.connect()
    result = db.select_rows(query)
    return result


def get_download_year(category, year):
    query = f"""
    SELECT t._id, t.buyer_id , t.buyer_name , t.cycle , t.date , t.expedition_day , t.expedition_month,
    t.expedition_trimester , t.expedition_year , t.tag,
    p.name , p._id , p.roles , p.identifier_schema , p.identifier_uri , p.street_address , p.locality_address,
    p.region_address , p.postal_code , p.country_name , p.contact_name , p.contact_email , p.contact_telephone , p.contact_fax 
    FROM {category} as t JOIN parties as p ON t._id = p.entry_id
    WHERE t.expedition_year = {year}
    """
    db.connect()
    result = db.select_rows(query)
    return result


def get_download_month(category, year, month):
    query = f"""
    SELECT t._id, t.buyer_id , t.buyer_name , t.cycle , t.date , t.expedition_day , t.expedition_month,
    t.expedition_trimester , t.expedition_year , t.tag,
    p.name , p._id , p.roles , p.identifier_schema , p.identifier_uri , p.street_address , p.locality_address,
    p.region_address , p.postal_code , p.country_name , p.contact_name , p.contact_email , p.contact_telephone , p.contact_fax  
    FROM {category} as t JOIN parties as p ON t._id = p.entry_id
    WHERE t.expedition_year = {year} and t.expedition_month = {month}
    """
    db.connect()
    result = db.select_rows(query)
    return result


def get_download_trimester(category, year, trimester):
    query = f"""
    SELECT t._id, t.buyer_id , t.buyer_name , t.cycle , t.date , t.expedition_day , t.expedition_month,
    t.expedition_trimester , t.expedition_year , t.tag,
    p.name , p._id , p.roles , p.identifier_schema , p.identifier_uri , p.street_address , p.locality_address,
    p.region_address , p.postal_code , p.country_name , p.contact_name , p.contact_email , p.contact_telephone , p.contact_fax  
    FROM {category} as t JOIN parties as p ON t._id = p.entry_id
    WHERE t.expedition_year = {year} and t.expedition_trimester = {trimester}
    """
    db.connect()
    result = db.select_rows(query)
    return result
