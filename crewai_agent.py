from crewai import Agent, Crew, Task
from langchain_community.chat_models import ChatOllama

local_llm = ChatOllama(
    model="llama3.2:3b",
    base_url="http://localhost:11434",
)

gamer_assistant = Agent(
    role="Gaming Catalog Critic",
    goal="Rank three video games based on immediate engagement value.",
    backstory="You are an algorithmic game reviewer who specializes in quick, fun gaming recommendations.",
    verbose=True,
    llm=local_llm,
)

triage_task = Task(
    description="Compare these three games: Warframe, Necesse, and Civ 6. Pick one for a fun evening session and give a 3-sentence reason why.",
    expected_output="A 3-sentence gaming suggestion.",
    agent=gamer_assistant,
)

crew = Crew(
    agents=[gamer_assistant],
    tasks=[triage_task],
    verbose=True,
)

print("\n--- AGENT STARTING RUN ---\n")
result = crew.kickoff()
print("\n--- AGENT RESPONSE ---")
print(result)