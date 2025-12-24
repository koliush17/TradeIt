from langchain_google_genai import ChatGoogleGenerativeAI

from app.schemas.env_schema import settings
from app.utils.logger import get_logger 

logger = get_logger("main")

def initialize_llm():
    llm = "gemini-2.5-flash"
    
    model = ChatGoogleGenerativeAI(
        model=llm,
        api_key=settings.GEMINI_API_KEY) 

    logger.info(f"Sucessfully setup a LLM: {llm}")

    return model 


