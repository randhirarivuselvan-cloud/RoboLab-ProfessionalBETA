from ai.base import Agent
class AuditorAgent(Agent):
    stage="audit"
    system_prompt="""You are RoboLab Final Auditor AI. Review ONLY the compiled project plus original requirements.
Determine whether the final project actually satisfies the original requirements. Do not claim zero errors or physical guarantees."""
    def model(self): return None
    def build_prompt(self,p,extra=None):
        return f"""Final audit.
ORIGINAL REQUIREMENTS: {p.user_requirements}
COMPILED PROJECT: {p.compiled_project}
Return JSON with decision (READY_FOR_REVIEW, NEEDS_CORRECTION, BLOCKED), findings, requirements_coverage. {extra or ''}"""
    def apply(self,p,r):
        p.audit_results=r.get("data",r)
        decision=p.audit_results.get("decision","NEEDS_CORRECTION")
        p.status=decision
        return p
