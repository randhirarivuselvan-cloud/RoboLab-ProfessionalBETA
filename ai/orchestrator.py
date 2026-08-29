from __future__ import annotations
from typing import Any
from core.models import Project
from core.config import AI_PROVIDER, AI_MODEL
from ai.providers import build_provider
from ai.agents import AGENTS
from services.validation import validate_cross_stage

class Orchestrator:
    def __init__(self):
        self.provider = build_provider(AI_PROVIDER)
    def provider_status(self):
        return {"provider": self.provider.name, "available": self.provider.available()}
    def run_stage(self, project: Project, stage: str, extra: str | None = None):
        if stage not in AGENTS and stage != "consensus":
            raise ValueError(f"Unknown stage: {stage}")
        if stage == "consensus":
            from ai.consensus import consensus
            return consensus.evaluate(project)
        agent = AGENTS[stage]
        project.stages.setdefault(stage, {"status":"waiting"})
        project.stages[stage].status = "running"
        prompt = agent.build_prompt(project, extra)
        if not self.provider.available():
            result = {"status":"failed","stage":stage,"error_code":"AI_PROVIDER_NOT_CONFIGURED",
                      "message":"No AI provider/API key is configured. Configure server-side environment variables before running generative AI stages.",
                      "recoverable":True}
            project.stages[stage].status = "failed"
            project.stages[stage].error = result
            project.errors.append(result["message"])
            project.status = "NEEDS_CONFIGURATION"
            return project
        result = self.provider.generate(agent.system_prompt, prompt, agent.model())
        if result.get("status") == "failed":
            project.stages[stage].status = "failed"
            project.stages[stage].error = result
            project.errors.append(result.get("message","AI stage failed"))
            return project
        project = agent.apply(project, result)
        project.stages[stage].status = "passed"
        project.stages[stage].output = result
        project.revision_history.append({"stage":stage,"action":"completed","result_status":"passed"})
        issues = validate_cross_stage(project)
        if issues:
            project.warnings.extend(issues)
        return project

orchestrator = Orchestrator()
