import httpx
from app.utils.logger import get_logger
from app.schemas.fear_greed_idx_schema import FearGreedIndexSchema
from datetime import datetime
from typing import Dict, List

class GetFearGreedIndex:
    def __init__(self):
        self.logger = get_logger("main")
        self.url = 'https://api.alternative.me/fng/'

    async def fetch_fear_greed_index(self) -> FearGreedIndexSchema:
        """Fetch fear and greed index"""
        extracted_data = await self._get_fear_greed_idx()
        processed_values = self._extract_fear_greed_data(extracted_data)

        return processed_values
        
    async def _get_fear_greed_idx(self) -> Dict:
        try:
            async with httpx.AsyncClient() as client:
                response = await client.get(self.url)
                response.raise_for_status()
                data = response.json()

        except httpx.HTTPError as e:
            self.logger.error(f"HTTP Error during extracting fear and greed index: {str(e)}")
            raise 

        except Exception as e:
            self.logger.exception(f"Unexpected error during extracting fear and greed index: {str(e)}")
            raise

        self.logger.info(f"Successfully extracted fear and greed index!")
        return data

    def _extract_fear_greed_data(self, data: Dict) -> List[FearGreedIndexSchema]:
        """Extract fear greed index"""

        try:
            index_info = FearGreedIndexSchema(
                classification = data["data"][0]["value_classification"],
                value = data["data"][0]["value"],
                time_stamp = self._convert_unix_timestamp(data["data"][0]["timestamp"])
            )
        
        except KeyError as e:
            self.logger.error(f"Missing expected filed in API response: {str(e)}")
            raise

        except Exception as e:
            self.logger.exception(f"Unexpected error during values extraction: {str(e)}")
            raise

        return index_info 

    @staticmethod
    def _convert_unix_timestamp(time_stamp: str) -> str:
        ts = int(time_stamp)
        value = datetime.fromtimestamp(ts)
        return value.strftime("%Y-%m-%d") 

