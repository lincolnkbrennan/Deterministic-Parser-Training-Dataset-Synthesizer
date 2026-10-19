import json

from dataset_tools.llm.mock import MockLLMClient, ValidMockLLMClient


def test_valid_mock_client_contract():
    client = ValidMockLLMClient()

    result = client.generate("test prompt", 1024)
    payload = json.loads(result)

    assert set(payload) == {
        "instruction",
        "context",
        "response",
    }


def test_invalid_mock_client_contract():
    client = MockLLMClient()

    result = client.generate("test prompt", 1024)
    payload = json.loads(result)

    assert "command" in payload
    assert "instruction" not in payload
