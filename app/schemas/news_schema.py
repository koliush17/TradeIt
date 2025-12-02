from pydantic import BaseModel
from datetime import date

class CryptoNewsDataSchema(BaseModel):
    title: str 
    summary: str 
    date_published: date 
    currency: str 
    relevance_score: float 
    ticker_sentiment_score: float




