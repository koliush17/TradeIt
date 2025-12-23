from fastapi import FastAPI 
from fastapi.responses import JSONResponse

from app.database.lifespan import lifespan 
from app.api import fetch_news, fetch_prices, fetch_fear_greed, fetch_intraday_prices, analyze_price, health
from app.exceptions import ExternalAPIError, DataParsingError, InvalidCryptoNameError

app = FastAPI(lifespan=lifespan)
app.include_router(fetch_news.router)
app.include_router(fetch_prices.router)
app.include_router(fetch_fear_greed.router)
app.include_router(fetch_intraday_prices.router)
app.include_router(analyze_price.router)
app.include_router(health.router)


@app.exception_handler(ExternalAPIError)
async def external_api_handler(request, exc):
    return JSONResponse(status_code=502, content={"error": exc.message})

@app.exception_handler(DataParsingError)
async def parsing_handler(request, exc):
    return JSONResponse(status_code=500, content={"error": exc.message})

@app.exception_handler(InvalidCryptoNameError)
async def invalid_cryptoname_handler(request, exc):
    return JSONResponse(status_code=400, content={"error": exc.message})   
