from google.adk.agents import Agent
from google.adk.agents.remote_a2a_agent import RemoteA2aAgent
from dotenv import load_dotenv
load_dotenv()

# A2A (Agent-to-Agent) Remote Connection Example
# 
# This agent connects to Dora remotely via A2A protocol.
# Dora must be running as an A2A server on port 8001.
#
# Setup:
# 1. Start Dora as A2A server: python -m adk_app.dora_a2a_server
# 2. Run this tourist agent: adk web adk_app --port 8000
# 3. Select "tourist" agent and chat!

# Create a remote reference to Dora
# The agent_card URL points to Dora's A2A discovery endpoint
dora_remote = RemoteA2aAgent(
    name="dora_remote",
    description="Remote connection to Dora the Explorer who knows capital cities.",
    agent_card="http://localhost:8001/.well-known/agent.json",
)

# Tourist agent that delegates to remote Dora
root_agent = Agent(
    name="tourist_agent",
    description="A clueless backpacker who asks Dora about capital cities remotely.",
    model="gemini-2.5-flash",
    instruction="""
    You are a clueless, excited backpacker traveling the world. 
    
    When the user mentions a country, you want to know its capital city so you don't 
    look silly. Delegate to the 'dora_remote' agent to find out capital cities.
    
    Be enthusiastic and grateful when you get answers!
    """,
    sub_agents=[dora_remote]  # Use sub_agents for agent delegation
)