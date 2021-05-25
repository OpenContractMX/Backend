CREATE TABLE comunicacion_transporte (
    id SERIAL PRIMARY KEY,
    _id VARCHAR(30) NOT NULL,
    buyer_id VARCHAR(30) NOT NULL,
    buyer_name VARCHAR(100) NOT NULL,
    cycle REAL NOT NULL,
    date TIMESTAMP NOT NULL,
    expedition_day REAL NOT NULL,
    expedition_month REAL NOT NULL,
    expedition_trimester REAL NOT NULL,
    expedition_year REAL NOT NULL,
    tag VARCHAR(50) NOT NULL
)

\copy comunicacion_transporte(_id, buyer_id, buyer_name, cycle, date, expedition_day, expedition_month, expedition_trimester, expedition_year, tag) from 'comunicacion_transporte_dfWoHeaders.csv' with DELIMITER '~';