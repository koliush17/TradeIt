from fastapi import APIRouter, Depends
from app.dependencies import get_conn

from app.dependencies import get_price_fetcher
from typing import Dict

router = APIRouter()

@router.post("/get_prices")
async def add_prices(currency: str, period: str = "DAILY", conn=Depends(get_conn)) -> Dict:
    price_class_cached = get_price_fetcher()
    prices = await price_class_cached.fetch_prices(currency, period)
    async with conn.cursor() as cursor:
        for doc in prices:
            await cursor.execute("""INSERT INTO crypto_prices
                                    (price_date, currency, time_period, open_price, highest_price,
                                    lowest_price, close_price, volume)

                                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
                                    ON CONFLICT (price_date, currency, time_period) DO NOTHING""",
                                    
                                    (doc.date_price, doc.currency, doc.time_period, doc.open_price, doc.high,
                                     doc.low, doc.close, doc.volume))

        await conn.commit()


    return {"message": f"Successfully fetched prices for {currency}!"}
