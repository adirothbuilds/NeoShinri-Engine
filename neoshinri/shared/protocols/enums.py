# Copyright (c) 2025 Adi Roth
# Part of the NeoShinri Project – https://github.com/adirothbuilds/NeoShinri
# Licensed under the NSPL License (see LICENSE file for details)

from enum import Enum

""" Enum for sender types in the acp protocol's schema."""
class SenderType(str, Enum):
    AGENT = "agent"
    USER = "user"
    CONTROLLER = "controller"
    SERVICE = "service"
    SYSTEM = "system"

""" Enum for receiver types in the acp protocol's schema."""
class ReceiverType(str, Enum):
    AGENT = "agent"
    USER = "user"
    CONTROLLER = "controller"
    SERVICE = "service"
    SYSTEM = "system"

""" Enum for message types in the acp protocol's schema."""
class MessageType(str, Enum):
    REQUEST = "request"
    RESPONSE = "response"
    NOTIFICATION = "notification"
    ERROR = "error"

class Priority(str, Enum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
    CRITICAL = "critical"