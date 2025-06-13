# Agent Communication Protocol (ACP) Schema

The Agent Communication Protocol (ACP) schema is a foundational component of the NeoShinri project. It defines the structure and behavior of entities involved in communication within the system. Below is an overview of the key components of the ACP schema.

## ACPMessage

The `ACPMessage` class is the core component of the ACP schema. It represents a message exchanged between agents, controllers, and other entities in the NeoShinri system. The class is implemented using the `pydantic` library and provides the following attributes and methods:

### Attributes

- **acp_version**: The version of the Agent Communication Protocol (ACP). Default: `1.0.0`.
- **sender**: The sender of the message. Example: `{ "uuid": "123e4567-e89b-12d3-a456-426614174000", "name": "Agent Alpha", "sender_type": "agent" }`.
- **receiver**: The receiver of the message. Example: `{ "uuid": "123e4567-e89b-12d3-a456-426614174001", "name": "Controller Beta", "receiver_type": "controller" }`.
- **message_type**: The type of the message. Default: `notification`. Example: `notification`.
- **content**: The content of the message. Example: `{ "instruction": "Execute task X", "tone": "polite", "language": "en-US" }`.
- **task_uuid**: A unique identifier for the task associated with the message. Example: `123e4567-e89b-12d3-a456-426614174002`.
- **timestamp**: The timestamp of the message. Default: Current datetime. Example: `2025-06-13T12:00:00`.
- **priority**: The priority of the message. Example: `high`.
- **context_uuid**: A unique identifier for the context associated with the message. Example: `123e4567-e89b-12d3-a456-426614174003`.
- **metadata**: Optional metadata associated with the message. Example: `{ "platform": "web", "user_role": "developer", "agent_traits": { "toolchain": ["read_file"], "language": "en-US", "temperature": 0.7 } }`.

### Methods

- **`__str__()`**: Returns a string representation of the `ACPMessage` instance.
- **`__log__(level: str = "info")`**: Logs the message information at a specified logging level. Default level is `info`.

## Summary

The `ACPMessage` class is the backbone of the ACP schema, enabling structured and consistent communication within the NeoShinri system. By leveraging `pydantic` models, it ensures data validation and clarity in message exchange.
