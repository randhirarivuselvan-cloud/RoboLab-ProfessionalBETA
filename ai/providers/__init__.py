from ai.providers.none import NoneProvider
from ai.providers.openai_provider import OpenAIProvider
from ai.providers.anthropic_provider import AnthropicProvider
from ai.providers.google_provider import GoogleProvider
from ai.providers.local_provider import LocalProvider

def build_provider(name):
    return {
        "none": NoneProvider,
        "openai": OpenAIProvider,
        "openai_compatible": OpenAIProvider,
        "anthropic": AnthropicProvider,
        "google": GoogleProvider,
        "gemini": GoogleProvider,
        "local": LocalProvider,
    }.get(name, NoneProvider)()
