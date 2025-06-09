import json
from typing import Any, Dict
from .constants import MessageType

class ACPMessage:
    """
    Base class for the Agent Communication Protocol (ACP) schema.
    Represents a message exchanged between AI agents.
    """

    def __init__(self, sender: str, receiver: str, message_type: MessageType, content: Dict[str, Any]):
        """
        Initialize an ACPMessage.

        :param sender: The ID of the agent sending the message.
        :param receiver: The ID of the agent receiving the message.
        :param message_type: The type of the message (e.g., MessageType.QUERY, MessageType.RESPONSE).
        :param content: The content of the message as a dictionary.
        """
        self.sender = sender
        self.receiver = receiver
        self.message_type = MessageType(message_type)
        self.content = content

    def to_dict(self) -> Dict[str, Any]:
        """
        Convert the ACPMessage to a dictionary.

        :return: A dictionary representation of the message.
        """
        return {
            "sender": self.sender,
            "receiver": self.receiver,
            "message_type": self.message_type.value,
            "content": self.content,
        }

    def to_json(self) -> str:
        """
        Encode the ACPMessage as a JSON string.

        :return: A JSON string representation of the message.
        """
        return json.dumps(self.to_dict())

    @staticmethod
    def from_dict(data: Dict[str, Any]) -> "ACPMessage":
        """
        Decode an ACPMessage from a dictionary.

        :param data: A dictionary representation of the message.
        :return: An ACPMessage instance.
        """
        return ACPMessage(
            sender=data["sender"],
            receiver=data["receiver"],
            message_type=MessageType(data["message_type"]),
            content=data["content"],
        )

    @staticmethod
    def from_json(json_str: str) -> "ACPMessage":
        """
        Decode an ACPMessage from a JSON string.

        :param json_str: A JSON string representation of the message.
        :return: An ACPMessage instance.
        """
        data = json.loads(json_str)
        return ACPMessage.from_dict(data)


# Helper functions
def encode_acp_message(sender: str, receiver: str, message_type: MessageType, content: Dict[str, Any]) -> str:
    """
    Helper to encode an ACPMessage to JSON.

    :param sender: The ID of the agent sending the message.
    :param receiver: The ID of the agent receiving the message.
    :param message_type: The type of the message (MessageType).
    :param content: The content of the message.
    :return: A JSON string representation of the message.
    """
    message = ACPMessage(sender, receiver, message_type, content)
    return message.to_json()


def decode_acp_message(json_str: str) -> ACPMessage:
    """
    Helper to decode a JSON string into an ACPMessage.

    :param json_str: A JSON string representation of the message.
    :return: An ACPMessage instance.
    """
    return ACPMessage.from_json(json_str)