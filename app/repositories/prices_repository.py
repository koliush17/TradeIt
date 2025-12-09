from typing import List 

from app.schemas.prices_schema import CryptoPricesDataSchema


async def insert_prices(conn, prices: List[CryptoPricesDataSchema]):
    async with conn.cursor() as cursor:
        for doc in prices:
            await cursor.execute("""INSERT INTO crypto_prices
                                    (price_date, currency, time_period, interval, open_price, highest_price,
                                    lowest_price, close_price, volume)

                                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
                                    ON CONFLICT (price_date, currency, time_period, interval) DO NOTHING""",
                                    
                                    (doc.date_price, doc.currency, doc.time_period,
                                     doc.interval, doc.open_price, doc.high,
                                     doc.low, doc.close, doc.volume))

        await conn.commit()


