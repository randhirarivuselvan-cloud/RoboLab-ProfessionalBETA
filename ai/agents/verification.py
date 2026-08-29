from ai.base import Agent
class VerificationAgent(Agent):
    stage="verify"
    system_prompt="""You are an independent RoboLab engineering verification AI. Do not merely repeat previous AI output.
Actively search for contradictions, missing requirements, incompatible components, incorrect assumptions, pin inconsistencies,
power problems, impossible specifications, safety considerations, and software/hardware mismatches."""
    def model(self): return None
    def build_prompt(self,p,extra=None):
        return f"""Review the unified project independently.
REQUIREMENTS: {p.user_requirements}
ARCHITECTURE: {p.architecture}
CIRCUIT: {p.connections} / {p.pin_map} / {p.power_budget}
FIRMWARE: {p.firmware}
CAD: {p.cad_specification}
Return JSON: findings=[{{severity,element,message,recommendation}}], summary. {extra or ''}"""
    def apply(self,p,r):
        d=r.get("data",r)
        p.verification_results.extend(d.get("findings",[]))
        return p
