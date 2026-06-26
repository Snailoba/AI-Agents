from google.adk.agents import Agent
from google.adk.tools import FunctionTool
from dotenv import load_dotenv
load_dotenv()

# 1. Create a simple local python function (The Tool)
def get_capital_city(country: str) -> str:
    """Retrieves the capital city of a given country."""
    capitals = {
        "thailand": "Bangkok",
        "germany": "Berlin",
        "japan": "Tokyo"
    }
    return capitals.get(country.lower(), "I don't know that country yet.")

# 2. Turn it into an ADK compliant tool
capital_tool = FunctionTool(get_capital_city)

# 3. Hand the tool to Dora the Explorer
root_agent = Agent(
    name="dora_explorer",
    description="Teaches users about capital cities around the world.",
    model="gemini-2.5-flash",
    instruction="""
    You are Dora the Explorer. Teach the user about capital cities around the world.
    
    CRITICAL RULES FOR TOOL USE:
    1. You ONLY possess the 'get_capital_city' tool. Do NOT attempt to invent or call any other tool names.
    2. If the user asks about a country's CAPITAL, you MUST use the 'get_capital_city' tool.
    3. If the user asks ANY general question that is NOT about a capital city (e.g., food, culture, hobbies, sea urchins), do NOT use a tool. Just answer immediately from your own general knowledge in character!
    """,
    tools=[capital_tool]
)