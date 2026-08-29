from ai.base import Agent
class CompilerAgent(Agent):
    stage="compile"
    system_prompt="""You are RoboLab Compiler AI. Integrate validated artifacts into ONE unified project.
Resolve inconsistencies using the canonical design or return the project for correction. Never silently choose a conflicting value."""
    def model(self): return None
    def build_prompt(self,p,extra=None):
        return f"""Compile this project into one coherent engineering project.
REQUIREMENTS: {p.user_requirements}
ARCHITECTURE: {p.architecture}
CIRCUIT: {p.components}, {p.connections}, {p.pin_map}
FIRMWARE: {p.firmware}
CAD: {p.cad_specification}
VERIFICATION: {p.verification_results}
Return JSON with compiled_project, unresolved_conflicts, status. {extra or ''}"""
    def apply(self,p,r):
        p.compiled_project=r.get("data",r)
        return p
