from fastapi import FastAPI, HTTPException, Request
from neoshinri.shared.protocols.acp import ACPMessage
from neoshinri.shared.protocols.constants import MessageType

app = FastAPI()


# Placeholder for Dispatcher
def dispatcher(message: dict):
    """
    Routes the message to the correct Agent REST endpoint.
    """
    # Use 'message_type' instead of 'type' for endpoint
    agent_endpoint = f"http://mock-agent/{message['message_type']}"
    return {"endpoint": agent_endpoint, "status": "mock-dispatched"}


# Placeholder for Memory Proxy
def memory_proxy():
    """
    Returns dummy context.
    """
    # TODO: Replace with actual memory proxy logic
    return {"context": "dummy-context"}


def acp_translator(message: dict):
    """
    Parses and validates incoming messages using ACPMessage and MessageType.
    Accepts both dict and JSON string body (from controller/main.py @app.post("/process")).
    """
    try:
        # If message is a JSON string, parse it
        import json

        if isinstance(message, str):
            message = json.loads(message)
        # If message is a dict with a single string value (from controller), parse that string
        if (
            isinstance(message, dict)
            and len(message) == 1
            and isinstance(next(iter(message.values())), str)
        ):
            # Try to parse the only value as JSON
            try:
                message = json.loads(next(iter(message.values())))
            except Exception:
                pass  # If not JSON, keep as is
        # Validate required fields
        if (
            "sender" not in message
            or "receiver" not in message
            or "message_type" not in message
            or "content" not in message
        ):
            raise HTTPException(status_code=400, detail="Invalid ACP message format")
        # Validate message_type
        if message["message_type"] not in MessageType._value2member_map_:
            raise HTTPException(status_code=400, detail="Invalid message_type")
        # Parse to ACPMessage
        acp_msg = ACPMessage.from_dict(message)
        return acp_msg
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"ACP translation error: {str(e)}")


@app.post("/tunnel")
async def tunnel(request: Request):
    """
    FastAPI endpoint to handle incoming messages.
    """
    try:
        message = await request.json()
        acp_message = acp_translator(message)
        dispatch_result = dispatcher(acp_message.to_dict())
        return {
            "status": "success",
            "dispatch_result": dispatch_result,
            "memory_context": memory_proxy(),
        }
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
