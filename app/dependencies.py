import psycopg 

from app.database.config import CONN_STRING
from functools import lru_cache

from app.market_data.get_news import GetNewsCrypto
from app.market_data.get_prices import GetPricesCrypto

async def get_conn():
    async with await psycopg.AsyncConnection.connect(CONN_STRING) as conn:
        yield conn

@lru_cache 
def get_news_fetcher() -> GetNewsCrypto:
    return GetNewsCrypto()

@lru_cache 
def get_price_fetcher() -> GetPricesCrypto:
    return GetPricesCrypto()

