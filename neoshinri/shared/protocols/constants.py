from enum import Enum

# Agent roles - these define the roles agents can take in the system
class Role(str, Enum):
    CONTROLLER = "controller"
    WORKER = "worker"
    OBSERVER = "observer"

# Message types - these are used to categorize the type of message being sent
class MessageType(str, Enum):
    QUERY = "query"
    RESPONSE = "response"
    COMMAND = "command"

# Task types - these are high-level categories of tasks that agents can perform
class TaskType(str, Enum):
    FILE_GENERATION = "file_generation"
    CODE_EXECUTION = "code_execution"
    SUMMARIZATION = "summarization"
