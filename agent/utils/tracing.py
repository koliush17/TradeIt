from app.schemas.env_schema import settings

from langfuse.langchain import CallbackHandler
from langfuse import Langfuse

langfuse = Langfuse(
    public_key=settings.LANGFUSE_PUBLIC_KEY,
    secret_key=settings.LANGFUSE_SECRET_KEY,
    host=settings.LANGFUSE_BASE_URL
)

langfuse_handler = CallbackHandler()
