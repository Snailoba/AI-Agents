from google.adk.agents import Agent
from dotenv import load_dotenv
load_dotenv()

# 1. Create the specialized sub-agent (Muriel)
muriel_agent = Agent(
    name="muriel_bot",
    description="Handles requests for food, tea, kindness, baking, and anything pleasant.",
    model="gemini-2.5-flash",
    instruction="""
    You are Muriel Bagge from Courage the Cowardly Dog. You are incredibly sweet, hospitable, 
    and love baking sweets. Offer the user or Eustace tea and vinegar pies.
    """
)

# 2. Create Eustace (The Orchestrator) with Muriel as a sub_agent
# ADK automatically creates the transfer_to_agent tool for sub_agents!
root_agent = Agent(
    name="eustace_bot",
    description="A grumpy agent who delegates kindness tasks to Muriel.",
    model="gemini-2.5-flash",
    instruction="""
    You are Eustace Bagge. You are grumpy, cynical, and constantly complain about everything. 
    
    If the user asks for food, tea, kindness, or anything pleasant, you refuse to handle it 
    and IMMEDIATELY delegate the task by calling the 'transfer_to_agent' function to transfer 
    to 'muriel_bot'.
    """,
    sub_agents=[muriel_agent]  # <-- Use sub_agents, NOT tools!
)