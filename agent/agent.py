from agent.prompts.system_prompt import SYSTEM_PROMPT 
from agent.utils.llm_model import initialize_llm  
from langchain.agents import create_agent
from langchain.agents.structured_output import ToolStrategy
from agent.schemas.tool_final_output_schema import AgentOutput

from agent.tools.get_fear_greed_index import get_fear_greed_index
from agent.tools.fetch_intraday_prices import fetch_intraday_prices
from agent.tools.fetch_longterm_prices import fetch_longterm_prices 
from agent.tools.fetch_news import fetch_news 
from agent.tools.get_news import get_news
from agent.tools.get_prices import get_prices

tools = [fetch_longterm_prices, fetch_news, fetch_intraday_prices, get_fear_greed_index, get_prices, get_news]

def initialize_agent():
    """Initialize ReAct agent"""

    model = initialize_llm()

    react_agent = create_agent(
        model=model,
        tools=tools,
        system_prompt=SYSTEM_PROMPT,
        response_format=ToolStrategy(AgentOutput))

    return react_agent
       


