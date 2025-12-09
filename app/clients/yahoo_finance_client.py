import yfinance as yf 

from app.utils.logger import get_logger
from app.exceptions import InvalidCryptoNameError

class YahooFinanceClient:
    def __init__(self):
        self.logger = get_logger("main")

    def fetch(self, currency: str, time_stamp: str = "1d", interval: str = "1h"):
        """Fetch information about crypto prices given the user parameters"""

        try:
            curr = yf.Ticker(f"{currency}-USD")
            historical_data = curr.history(period=time_stamp, interval=interval)

        except KeyError as e:
            self.logger.error(f"Invalid cryptocurrency name provided: {str(e)}")
            raise InvalidCryptoNameError("Yahoo Finance", f"Invalid crypto name: {currency}")

        except Exception as e:
            self.logger.error(f"During extracting intraday prices the error happened: {str(e)}")
            raise

        return historical_data




