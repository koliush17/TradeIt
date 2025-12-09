from fastapi import APIRouter, Depends

from app.dependencies import get_conn
from app.dependencies import get_intraday_price_fetcher 
from app.repositories.prices_repository import insert_prices 

from typing import Dict

router = APIRouter()

@router.post("/get_intraday_prices")
async def add_intraday_prices(currency: str, 
                              time_stamp: str = "1d",
                              interval: str = "1h",
                              conn=Depends(get_conn)) -> Dict:

    intraday_class_cached = get_intraday_price_fetcher()

    prices = await intraday_class_cached.fetch_intraday_prices(currency,
                                                               time_stamp,
                                                               interval)
    await insert_prices(conn, prices)

    return {"message": "Successfully inserted intraday prices to database"}



