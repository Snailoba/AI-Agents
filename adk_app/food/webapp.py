import streamlit as st
import asyncio
import os
from dotenv import load_dotenv
from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService
from google.genai import types
# Import the root agent you already built
from agent import root_agent

# Load environment variables from .env file
load_dotenv()

st.title("🍔 Food Reviews")
st.write("Extracting structured review analytics from local CSV repositories.")

# 1. UI Dropdown menu for the user
dish = st.selectbox("Select a menu item to analyze:", ["Matcha Latte", "Smoked Salmon", "Pork Chops", "Steak", "Bolognese", "Panna Cotta", "Strawberry Smoothie", "Pesto"])

async def run_agent_async(query: str):
    """Async function to run the ADK agent."""
    session_service = InMemorySessionService()
    
    # Create a session
    session = await session_service.create_session(
        app_name="food_app",
        user_id="user1"
    )
    
    # Create a runner
    runner = Runner(
        agent=root_agent,
        app_name="food_app",
        session_service=session_service
    )
    
    # Create the message
    content = types.Content(
        role='user',
        parts=[types.Part(text=query)]
    )
    
    # Run the agent and collect the response
    final_response = ""
    async for event in runner.run_async(
        user_id="user1",
        session_id=session.id,
        new_message=content
    ):
        if event.is_final_response() and event.content and event.content.parts:
            final_response = event.content.parts[0].text
    
    return final_response if final_response else "No response received from agent."

if st.button("Run ADK Analysis"):
    with st.spinner("Invoking ADK agent and filtering local data structures..."):
        # 2. Trigger the agent via ADK Runner
        query = f"Analyze the {dish}"
        try:
            response = asyncio.run(run_agent_async(query))
            st.success("Analysis Complete!")
            # 3. Render clean visual blocks on the dashboard
            st.subheader(f"System Assessment for: {dish}")
            st.info(response)
        except Exception as e:
            st.error(f"Error running agent: {str(e)}")
            st.info("Make sure your GOOGLE_API_KEY is set correctly in the .env file.")