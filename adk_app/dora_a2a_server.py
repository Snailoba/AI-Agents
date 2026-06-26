"""
A2A Server for Dora the Explorer agent.

This creates an A2A (Agent-to-Agent) server that exposes Dora remotely.
Other agents can connect via HTTP to interact with Dora.

Usage:
    Terminal 1: python -m adk_app.dora_a2a_server
    Terminal 2: adk web adk_app --port 8000
    Then select "tourist" agent which connects to Dora remotely.
"""

import uvicorn
from dotenv import load_dotenv

load_dotenv()

from adk_app.dora.agent import root_agent as dora_agent

# A2A components (0.3.26 API)
from a2a.server.apps import A2AStarletteApplication
from a2a.server.request_handlers import DefaultRequestHandler
from a2a.server.tasks import InMemoryTaskStore, InMemoryPushNotificationConfigStore
from a2a.types import AgentCard, AgentCapabilities

# ADK components
from google.adk.a2a.executor.a2a_agent_executor import A2aAgentExecutor
from google.adk.runners import Runner
from google.adk.sessions.in_memory_session_service import InMemorySessionService
from google.adk.memory.in_memory_memory_service import InMemoryMemoryService
from google.adk.artifacts.in_memory_artifact_service import InMemoryArtifactService
from google.adk.auth.credential_service.in_memory_credential_service import InMemoryCredentialService

# Create runner for Dora
runner = Runner(
    app_name="dora",
    agent=dora_agent,
    session_service=InMemorySessionService(),
    memory_service=InMemoryMemoryService(),
    artifact_service=InMemoryArtifactService(),
    credential_service=InMemoryCredentialService(),
)

# Create A2A executor
executor = A2aAgentExecutor(runner=runner)

# Create task store
task_store = InMemoryTaskStore()
push_config_store = InMemoryPushNotificationConfigStore()

# Create request handler
request_handler = DefaultRequestHandler(
    agent_executor=executor,
    task_store=task_store,
    push_config_store=push_config_store,
)

# Create agent card
agent_card = AgentCard(
    name="Dora",
    description="Dora the Explorer knows capital cities of countries!",
    url="http://localhost:8001/",
    version="1.0.0",
    defaultInputModes=["text"],
    defaultOutputModes=["text"],
    capabilities=AgentCapabilities(
        streaming=True,
    ),
    skills=[],  # No specific skills defined
)

# Create A2A Starlette application
a2a_app = A2AStarletteApplication(
    agent_card=agent_card,
    http_handler=request_handler,
)
# Build the actual Starlette app
app = a2a_app.build()

if __name__ == "__main__":
    print("=" * 60)
    print("Dora A2A Server starting on http://localhost:8001")
    print("Agent card: http://localhost:8001/.well-known/agent.json")
    print("=" * 60)
    uvicorn.run(app, host="localhost", port=8001)