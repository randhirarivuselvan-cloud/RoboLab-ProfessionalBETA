from ai.base import Agent
class BuilderAgent(Agent):
    stage="builder"
    system_prompt="""You are RoboLab Builder AI, a universally professional robotics system/mechanical engineering generator.
Produce structured engineering artifacts. Respect known facts, explicitly mark assumptions, and never invent unknown facts.
You are one member of a synchronized engineering team; use the canonical project specification."""
    def model(self): return None
    def build_prompt(self,p,extra=None):
        return f"""Generate/refine the system architecture for this project.
IDEA: {p.metadata.get('idea','')}
REQUIREMENTS: {p.user_requirements}
CURRENT CANONICAL SPEC: {p.model_dump_json()}
Return JSON with requirements, assumptions, constraints, architecture, components, mechanical_design, cad_specification. {extra or ''}"""
    def apply(self,p,r):
        d=r.get("data",r)
        for k in ("assumptions","constraints","architecture","components","mechanical_design","cad_specification"):
            if k in d: setattr(p,k,d[k])
        return p
