from fastapi import APIRouter, Depends
from psycopg import AsyncConnection, OperationalError
from app.dependencies import get_conn

router = APIRouter(tags=["Health"])

@router.get("/health")
async def health():
    """Check liveness of the process"""

    return {"status": "healthy"}

@router.get("/ready")
async def ready(conn: AsyncConnection = Depends(get_conn)):
    """Check liveness of the database"""

    try:
        async with conn.cursor() as cursor:
            await cursor.execute("SELECT 1")

        return {"status": "ready", "database": "connected"}

    except OperationalError:
        return {"status": "not ready", "database": "disconnected"}
                
            

