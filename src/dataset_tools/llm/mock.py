from pathlib import Path


class MockLLMClient:
    """
    Negative test client.

    Returns malformed model output to exercise
    parser/validator rejection paths.
    """

    def generate(self, prompt: str, max_tokens: int) -> str:
        return '{"command":"fake"}'


class ValidMockLLMClient:
    """
    Positive test client.

    Returns schema-valid model output for
    provider contract tests.
    """

    def generate(self, prompt: str, max_tokens: int) -> str:
        fixture = Path("tests/fixtures/llm_valid_response.json")
        return fixture.read_text(encoding="utf-8")
