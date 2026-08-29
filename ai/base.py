from abc import ABC, abstractmethod
from typing import Any
from core.models import Project

class AIProvider(ABC):
    name = "base"
    @abstractmethod
    def available(self) -> bool: ...
    @abstractmethod
    def generate(self, system: str, prompt: str, model: str | None = None) -> dict[str, Any]: ...

class Agent(ABC):
    stage = ""
    @abstractmethod
    def build_prompt(self, project: Project, extra: str | None = None) -> str: ...
    def apply(self, project: Project, result: dict[str, Any]) -> Project:
        return project
