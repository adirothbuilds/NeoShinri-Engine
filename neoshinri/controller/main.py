from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import requests
import uuid
from neoshinri.shared.protocols.acp import ACPMessage
from neoshinri.shared.protocols.constants import TaskType, Role, MessageType
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Initialize FastAPI app
app = FastAPI()


# Define models
class UserRequest(BaseModel):
    user_input: str


class Task(BaseModel):
    task_id: str
    task_type: MessageType
    description: str


def generate_tasks(user_input: str):
    # For now, return a static task
    logger.info(f"Generating task for user input: {user_input}")
    return Task(
        task_id=str(uuid.uuid4()),
        task_type=MessageType.COMMAND,
        description="Generate a file based on user input: " + user_input,
    )


# Router logic to dispatch to a predefined agent role
def route_task(task: Task) -> Role:
    # For now, route all tasks to a single predefined agent role
    logger.info(f"Routing task {task.task_id} of type {task.task_type}")
    if task.task_type == TaskType.FILE_GENERATION:
        return Role.CONTROLLER
    return Role.WORKER


# Create ACPMessage
def create_acp_message(agent_role: str, task: Task):
    logger.info(f"Creating ACPMessage for task {task.task_id} to agent role {agent_role}")
    return ACPMessage(
        sender="user", receiver=agent_role, message_type=task.task_type, content=task.description
    )


# Send ACPMessage to Tunnel
def send_to_tunnel(acp_message: ACPMessage):
    # Assume the Tunnel is a FastAPI gateway running at this URL
    try:
        tunnel_url = "http://localhost:8000/tunnel"  # FIX: use correct tunnel port
        logger.info(f"Sending ACPMessage to Tunnel at {tunnel_url}")
        response = requests.post(tunnel_url, json=acp_message.to_json(), timeout=5)
        response.raise_for_status()  # Raise an error for bad responses
        # Assuming the Tunnel returns a JSON response
        if not response.headers.get("Content-Type") == "application/json":
            logger.error("Tunnel did not return JSON response")
            raise HTTPException(status_code=500, detail="Tunnel did not return JSON response")
        # Parse the JSON response
        if response.status_code != 200:
            logger.error(f"Error from Tunnel: {response.status_code} - {response.text}")
            raise HTTPException(
                status_code=response.status_code, detail="Error from Tunnel: " + response.text
            )
        # Return the parsed JSON response
        logger.info("Received response from Tunnel")
        return response.json()
    except requests.exceptions.RequestException as e:
        logger.error(f"Error communicating with Tunnel: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Error communicating with Tunnel: {str(e)}")


# FastAPI endpoint
@app.post("/process")
def process_request(user_request: UserRequest):
    # Step 1: Task Planner
    logger.info(f"Received user request: {user_request.user_input}")
    task = generate_tasks(user_request.user_input)

    # Step 2: Router
    logger.info(f"Routing task: {task.task_id} of type {task.task_type}")
    agent_role = route_task(task)

    # Step 3: Create ACPMessage
    logger.info(f"Creating ACPMessage for task {task.task_id} to agent role {agent_role}")
    acp_message = create_acp_message(agent_role, task)

    # Step 4: Send to Tunnel
    logger.info(f"Sending ACPMessage to Tunnel: {acp_message.to_json()}")
    response = send_to_tunnel(acp_message)

    # Return the response from the Tunnel
    logger.info(f"Received response from Tunnel: {response}")
    return {"status": "success", "tunnel_response": response}
