from pydantic import BaseModel
from datetime import date

class CryptoPricesDataSchema(BaseModel):
    date_price : date
    currency: str
    time_period: str
    open_price: float 
    high: float 
    low: float
    close: float 
    volume: float


