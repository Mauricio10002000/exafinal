import psycopg2
## para recuperar datos de .env
from decouple import config

def conexion2023():
    conex=psycopg2.connect(
            host=config('PG_HOST'),
            user=config('PG_USER'),
            password=config('PG_PASSWORD'),
            database=config('PG_DB')
        )
    return conex