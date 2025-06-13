# Copyright (c) 2025 Adi Roth
# Part of the NeoShinri Project – https://github.com/adirothbuilds/NeoShinri
# Licensed under the NSPL License (see LICENSE file for details)

import datetime
import logging
from pydantic import BaseModel, Field
from uuid import UUID
from typing import Optional, List

from enums import SenderType, ReceiverType, MessageType, Priority

""" 
Base class for identities in the Agent Communication Protocol (ACP) schema.
Represents a unique identity with a UUID and an optional name.

Attributes:
- uuid: Unique identifier for the identity.
- name: Optional name of the identity.

Usefull Built-in Methods(from BaseModel):
- __init__: Initializes the identity with a UUID and an optional name.
- __str__: Returns a string representation of the identity
- json: Converts the identity to a JSON string.
- dict: Converts the identity to a dictionary.
- parse_obj: Parses a dictionary to create an instance of the identity.
- parse_raw: Parses a JSON string to create an instance of the identity.

Methods:
- __log__: Logs the identity information at a specified logging level.
"""
class ACPIdentity(BaseModel):
    uuid: UUID = Field(..., description="Unique identifier for the identity", example="123e4567-e89b-12d3-a456-426614174000")
    name: Optional[str] = Field(None, description="Name of the identity (optional)", example="Agent Alpha")

    def __log__(self, level: str = "info"):
        logger = logging.getLogger(__name__)
        if not logger.hasHandlers():
            logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
        log_message = f"[ {datetime.datetime.now()} ] - {self.__str__()}"
        getattr(logger, level.lower(), logger.info)(log_message)

"""
Sender class inherits from ACPIdentity.
Represents a sender in the Agent Communication Protocol (ACP) schema.
Includes a sender_type field to specify the type of sender.

Attributes:
- sender_type: Type of the sender (e.g., 'user', 'agent', 'controller', 'service', 'system').

Methods:
- __str__: Returns a string representation of the Sender instance.
"""
class Sender(ACPIdentity):
    sender_type: SenderType = Field(..., description="Type of the sender (e.g., 'user', 'agent', 'controller', 'service', 'system')", example="agent")
    
    def __str__(self):
        return f"Sender(uuid={self.uuid}, name={self.name}, sender_type={self.sender_type})"

"""
Receiver class inherits from ACPIdentity.
Represents a receiver in the Agent Communication Protocol (ACP) schema.
Includes a receiver_type field to specify the type of receiver.

Attributes:
- receiver_type: Type of the receiver (e.g., 'user', 'agent', 'controller', 'service', 'system').

Methods:
- __str__: Returns a string representation of the Receiver instance.
"""
class Receiver(ACPIdentity):
    receiver_type: ReceiverType = Field(..., description="Type of the receiver (e.g., 'user', 'agent', 'controller', 'service', 'system')", example="controller")
    
    def __str__(self):
        return f"Receiver(uuid={self.uuid}, name={self.name}, receiver_type={self.receiver_type})"

"""
Content class represents the content of a message in the Agent Communication Protocol (ACP) schema.

Attributes:
- instruction: Instruction for the agent.
- tone: Optional tone of the instruction.
- language: Optional language of the instruction.

Methods:
- __str__: Returns a string representation of the Content instance.
- __log__: Logs the content information at a specified logging level.
"""
class Content(BaseModel):
    instruction: str = Field(..., description="Instruction for the agent", example="Execute task X")
    tone: Optional[str] = Field(None, description="Tone of the instruction (optional)", example="polite")
    language: Optional[str] = Field(None, description="Language of the instruction (optional)", example="en-US")

    def __str__(self):
        return f"Content(instruction={self.instruction}, tone={self.tone}, language={self.language})"
    
    def __log__(self, level: str = "info"):
        logger = logging.getLogger(__name__)
        if not logger.hasHandlers():
            logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
        log_message = f"[ {datetime.datetime.now()} ] - {self.__str__()}"
        getattr(logger, level.lower(), logger.info)(log_message)

"""
AgentTraits class represents the traits of an agent in the Agent Communication Protocol (ACP) schema.

Attributes:
- toolchain: Optional tool chain used by the agent.
- language: Optional Desired language of the response..
- temperature: Optional temperature setting for the agent.

Methods:
- __str__: Returns a string representation of the AgentTraits instance.
- __log__: Logs the agent traits information at a specified logging level.
"""
class AgentTraits(BaseModel):
    toolchain: Optional[List[str]] = Field(None, description="Tool chain used by the agent (optional)", example=["read_file", "write_file"])
    language: Optional[str] = Field(None, description="Desired language of the response. (optional)", example="en-US")
    temperature: Optional[float] = Field(None, description="Temperature setting for the agent (optional)", example=0.7)

    def __str__(self):
        return f"AgentTraits(toolchain={self.toolchain}, language={self.language}, temperature={self.temperature})"
    
    def __log__(self, level: str = "info"):
        logger = logging.getLogger(__name__)
        if not logger.hasHandlers():
            logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
        log_message = f"[ {datetime.datetime.now()} ] - {self.__str__()}"
        getattr(logger, level.lower(), logger.info)(log_message)

"""
Metadata class represents additional metadata associated with a message in the Agent Communication Protocol (ACP) schema.

Attributes:
- platform: Optional platform information.
- user_role: Optional user role information.
- agent_traits: Optional traits of the agent.

Methods:
- __str__: Returns a string representation of the Metadata instance.
- __log__: Logs the metadata information at a specified logging level.
"""
class Metadata(BaseModel):
    platform: Optional[str] = Field(None, description="Platform information (optional)", example="web")
    user_role: Optional[str] = Field(None, description="User role information (optional)", example="developer")
    agent_traits: Optional[AgentTraits] = Field(None, description="Traits of the agent (optional)", example={"toolchain": ["read_file"], "language": "en-US", "temperature": 0.7})

    def __str__(self):
        return f"Metadata(platform={self.platform}, user_role={self.user_role}, agent_traits={self.agent_traits})"
    
    def __log__(self, level: str = "info"):
        logger = logging.getLogger(__name__)
        if not logger.hasHandlers():
            logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
        log_message = f"[ {datetime.datetime.now()} ] - {self.__str__()}"
        getattr(logger, level.lower(), logger.info)(log_message)

"""
ACPMessage class represents a message in the Agent Communication Protocol (ACP) schema.

Attributes:
- acp_version: Version of the Agent Communication Protocol (default is "1.0.0").
- sender: Sender of the message (instance of Sender).
- receiver: Receiver of the message (instance of Receiver).
- message_type: Type of the message (default is MessageType.NOTIFICATION).
- content: Content of the message (instance of Content).
- task_uuid: Unique identifier for the task associated with the message
- timestamp: Timestamp of the message (default is current time).
- priority: Priority of the message (instance of Priority).
- context_uuid: Unique identifier for the context associated with the message.
- metadata: Optional metadata associated with the message (instance of Metadata).

Methods:
- __str__: Returns a string representation of the ACPMessage instance.
- __log__: Logs the message information at a specified logging level.
"""
class ACPMessage(BaseModel):
    acp_version: str = Field(default="1.0.0", description="Version of the Agent Communication Protocol (ACP)", example="1.0.0")
    sender: Sender = Field(..., description="Sender of the message", example={"uuid": "123e4567-e89b-12d3-a456-426614174000", "name": "Agent Alpha", "sender_type": "agent"})
    receiver: Receiver = Field(..., description="Receiver of the message", example={"uuid": "123e4567-e89b-12d3-a456-426614174001", "name": "Controller Beta", "receiver_type": "controller"})
    message_type: MessageType = Field(default=MessageType.NOTIFICATION, description="Type of the message", example="notification")
    content: Content = Field(..., description="Content of the message", example={"instruction": "Execute task X", "tone": "polite", "language": "en-US"})
    task_uuid: UUID = Field(..., description="Unique identifier for the task associated with the message", example="123e4567-e89b-12d3-a456-426614174002")
    timestamp: datetime.datetime = Field(default_factory=datetime.datetime.now, description="Timestamp of the message", example="2025-06-13T12:00:00")
    priority: Priority = Field(..., description="Priority of the message", example="high")
    context_uuid: UUID = Field(..., description="Unique identifier for the context associated with the message", example="123e4567-e89b-12d3-a456-426614174003")
    metadata: Optional[Metadata] = Field(None, description="Metadata associated with the message (optional)", example={"platform": "web", "user_role": "developer", "agent_traits": {"toolchain": ["read_file"], "language": "en-US", "temperature": 0.7}})

    def __str__(self):
        return (f"ACPMessage(acp_version={self.acp_version}, sender={self.sender}, "
                f"receiver={self.receiver}, message_type={self.message_type}, "
                f"content={self.content}, task_uuid={self.task_uuid}, "
                f"timestamp={self.timestamp}, priority={self.priority}, "
                f"context_uuid={self.context_uuid}, metadata={self.metadata})")
    
    def __log__(self, level: str = "info"):
        logger = logging.getLogger(__name__)
        if not logger.hasHandlers():
            logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
        log_message = f"[ {datetime.datetime.now()} ] - {self.__str__()}"
        getattr(logger, level.lower(), logger.info)(log_message)