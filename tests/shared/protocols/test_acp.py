import pytest
from neoshinri.shared.protocols.acp import ACPMessage, encode_acp_message, decode_acp_message
from neoshinri.shared.protocols.constants import MessageType


@pytest.fixture
def acp_message():
    return ACPMessage(
        sender="agent_1",
        receiver="agent_2",
        message_type=MessageType.QUERY,
        content={"key": "value"},
    )


def test_acp_message_initialization(acp_message):
    """
    Test the initialization of ACPMessage with valid parameters.
    """
    assert acp_message.sender == "agent_1"
    assert acp_message.receiver == "agent_2"
    assert acp_message.message_type == MessageType.QUERY
    assert acp_message.content == {"key": "value"}


def test_acp_message_to_dict(acp_message):
    """
    Test the conversion of ACPMessage to a dictionary.
    """
    expected_dict = {
        "sender": "agent_1",
        "receiver": "agent_2",
        "message_type": MessageType.QUERY.value,
        "content": {"key": "value"},
    }
    assert acp_message.to_dict() == expected_dict


def test_acp_message_to_json(acp_message):
    """
    Test the conversion of ACPMessage to a JSON string.
    """
    expected_json = '{"sender": "agent_1", "receiver": "agent_2", "message_type": "query", "content": {"key": "value"}}'
    assert acp_message.to_json() == expected_json


def test_acp_message_from_dict(acp_message):
    """
    Test the creation of ACPMessage from a dictionary.
    """
    data = {
        "sender": "agent_1",
        "receiver": "agent_2",
        "message_type": MessageType.QUERY.value,
        "content": {"key": "value"},
    }
    message = ACPMessage.from_dict(data)
    assert message.sender == acp_message.sender
    assert message.receiver == acp_message.receiver
    assert message.message_type == acp_message.message_type
    assert message.content == acp_message.content


def test_acp_message_from_json(acp_message):
    """
    Test the creation of ACPMessage from a JSON string.
    """
    json_str = '{"sender": "agent_1", "receiver": "agent_2", "message_type": "query", "content": {"key": "value"}}'
    message = ACPMessage.from_json(json_str)
    assert message.sender == acp_message.sender
    assert message.receiver == acp_message.receiver
    assert message.message_type == acp_message.message_type
    assert message.content == acp_message.content


def test_encode_acp_message(acp_message):
    """
    Test the helper function to encode an ACPMessage to JSON.
    """
    json_str = encode_acp_message(
        sender=acp_message.sender,
        receiver=acp_message.receiver,
        message_type=acp_message.message_type,
        content=acp_message.content,
    )
    expected_json = '{"sender": "agent_1", "receiver": "agent_2", "message_type": "query", "content": {"key": "value"}}'
    assert json_str == expected_json


def test_decode_acp_message(acp_message):
    """
    Test the helper function to decode a JSON string to an ACPMessage.
    """
    json_str = '{"sender": "agent_1", "receiver": "agent_2", "message_type": "query", "content": {"key": "value"}}'
    message = decode_acp_message(json_str)
    assert message.sender == acp_message.sender
    assert message.receiver == acp_message.receiver
    assert message.message_type == acp_message.message_type
    assert message.content == acp_message.content
