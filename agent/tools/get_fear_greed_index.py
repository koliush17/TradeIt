import psycopg
from psycopg.rows import dict_row
from app.database.config import CONN_STRING 
from typing import List, Dict
from app.utils.logger import get_logger
from app.exceptions import DataBaseConnectionError

from langchain.tools import tool

logger = get_logger("main")

@tool
def get_fear_greed_index(limit: int = 10) -> List[Dict]:
    """Query database to get fear and greed index.

    Use this when you need to get information about fear and greed index.

    args:
        limit: maximum number of records to return

    returns:
        list of news records, each containing:
            - id: record id
            - classification: name of the current stage of the market
            - value: index of fear and greed
            - time_stamp: date of fetched index
            - fetched_at: when the data was fetched
    """
    try: 
        with psycopg.connect(CONN_STRING, row_factory=dict_row) as conn:
            with conn.cursor() as cur:
                cur.execute("""
                    SELECT classification, time_stamp, fetched_at
                    FROM fear_greed_index
                    ORDER BY fetched_at DESC
                    LIMIT %s;
                    """,
                    (limit, ))

                rows = cur.fetchall()

                return rows

    except ConnectionError:
        logger.critical("Unable to connect to database!")
        raise DataBaseConnectionError("Service unavailable")

    except Exception as e:
        logger.error(f"Unexpected database error: {str(e)}")
        raise


