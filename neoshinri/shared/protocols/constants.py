from enum import Enum

# Agent roles
default = object()  # to avoid linter errors for unused import

class Role(str, Enum):
    CONTROLLER = "controller"
    WORKER = "worker"
    OBSERVER = "observer"

class MessageType(str, Enum):
    QUERY = "query"
    RESPONSE = "response"
    COMMAND = "command"

class TaskType(str, Enum):
    FILE_GENERATION = "file_generation"
    CODE_EXECUTION = "code_execution"
    SUMMARIZATION = "summarization"
