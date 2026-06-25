from google.adk import Agent

# Define a native ADK agent
root_agent = Agent(
    name="backlog_manager",
    model="ollama/llama3.2:3b",  # It can route to your local Ollama setup!
    instruction="""
    You are a gaming triage assistant. Your job is to help the user manage their gaming backlog 
    (specifically Warframe, Voidling Bound, and Beastro). Keep your energy casual, 
    use modern gaming slang, and give brief, decisive recommendations.
    """
)