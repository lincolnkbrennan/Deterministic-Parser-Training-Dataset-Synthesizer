import pytest

from dataset_tools.llm.factory import create_llm_client
from dataset_tools.llm.mock import MockLLMClient


def test_mock_provider_creates_client():
    client = create_llm_client(
        provider="mock",
        endpoint="unused",
        model="mock",
    )

    assert isinstance(client, MockLLMClient)


def test_unknown_provider_fails():
    with pytest.raises(ValueError):
        create_llm_client(
            provider="does_not_exist",
            endpoint="unused",
            model="unknown",
        )
