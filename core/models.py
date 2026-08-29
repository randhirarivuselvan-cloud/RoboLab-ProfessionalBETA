from __future__ import annotations
from typing import Any, Literal
from pydantic import BaseModel, Field
from uuid import uuid4
from datetime import datetime, timezone

StageStatus = Literal["waiting","running","passed","warning","failed"]

def now():
    return datetime.now(timezone.utc).isoformat()

class Stage(BaseModel):
    status: StageStatus = "waiting"
    output: dict[str, Any] = Field(default_factory=dict)
    error: dict[str, Any] | None = None
    updated_at: str = Field(default_factory=now)

class ProjectCreate(BaseModel):
    name: str = Field(min_length=1, max_length=160)
    idea: str = Field(min_length=1, max_length=10000)
    requirements: list[str] = Field(default_factory=list)

class StageRunRequest(BaseModel):
    prompt: str | None = Field(default=None, max_length=10000)

class Project(BaseModel):
    name: str = "Untitled Project"
    project_id: str = Field(default_factory=lambda: str(uuid4()))
    user_requirements: list[str] = Field(default_factory=list)
    assumptions: list[str] = Field(default_factory=list)
    constraints: list[str] = Field(default_factory=list)
    architecture: dict[str, Any] = Field(default_factory=dict)
    components: list[dict[str, Any]] = Field(default_factory=list)
    connections: list[dict[str, Any]] = Field(default_factory=list)
    pin_map: list[dict[str, Any]] = Field(default_factory=list)
    power_budget: dict[str, Any] = Field(default_factory=dict)
    firmware: dict[str, Any] = Field(default_factory=dict)
    mechanical_design: dict[str, Any] = Field(default_factory=dict)
    cad_specification: dict[str, Any] = Field(default_factory=dict)
    simulation_results: dict[str, Any] = Field(default_factory=dict)
    verification_results: list[dict[str, Any]] = Field(default_factory=list)
    compiled_project: dict[str, Any] = Field(default_factory=dict)
    audit_results: dict[str, Any] = Field(default_factory=dict)
    status: str = "DRAFT"
    warnings: list[str] = Field(default_factory=list)
    errors: list[str] = Field(default_factory=list)
    revision_history: list[dict[str, Any]] = Field(default_factory=list)
    stages: dict[str, Stage] = Field(default_factory=dict)
    metadata: dict[str, Any] = Field(default_factory=dict)
    created_at: str = Field(default_factory=now)
    updated_at: str = Field(default_factory=now)

    def touch(self):
        self.updated_at = now()
