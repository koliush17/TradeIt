from fastapi import FastAPI 
from app.database.lifespan import lifespan 
from app.api import fetch_news, fetch_prices

app = FastAPI(lifespan=lifespan)
app.include_router(fetch_news.router)
app.include_router(fetch_prices.router)



