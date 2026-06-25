from crewai import Agent, Task, Crew, LLM

# 1. Connect to your local Ollama model
local_llm = LLM(
    model="ollama/llama3.2:3b",
    base_url="http://localhost:11434"
)

# 2. Define your Agent with zero "trigger" words
gamer_assistant = Agent(
    role="Gaming Catalog Critic",
    goal="Rank three video games based on immediate engagement value.",
    backstory="You are an algorithmic game reviewer who specializes in quick, fun gaming recommendations.",
    verbose=True,
    llm=local_llm
)

# 3. Define the completely safe Task
triage_task = Task(
    description="Compare these three games: Warframe, Voidling Bound, and Beastro. Pick one for a fun evening session and give a 3-sentence reason why.",
    expected_output="A 3-sentence gaming suggestion.",
    agent=gamer_assistant
)

# 4. Put the agent to work
crew = Crew(
    agents=[gamer_assistant],
    tasks=[triage_task],
    verbose=True
)

# Run it!
print("\n--- AGENT STARTING RUN ---\n")
result = crew.kickoff()
print("\n--- AGENT RESPONSE ---")
print(result)