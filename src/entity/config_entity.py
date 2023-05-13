from dataclasses import dataclass

@dataclass
class ChainConfig:
    chain_type: str = "stuff"
    verbose: bool = False


@dataclass
class MemoryConfig:
    memory_key: str = "chat_history"
    return_messages: bool = False

@dataclass
class OpenAIConfig:
    temperature: int = 0.5
