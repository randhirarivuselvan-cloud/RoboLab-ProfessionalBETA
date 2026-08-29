from ai.base import Agent
class CADAgent(Agent):
    stage="cad"
    system_prompt="""You are RoboLab CAD/Mechanical AI. Produce professional mechanical specifications tied to the canonical project.
Do not claim text-only CAD is equivalent to a validated physical model."""
    def model(self): return None
    def build_prompt(self,p,extra=None):
        return f"""Generate/refine CAD/mechanical specification from:
ARCHITECTURE: {p.architecture}
COMPONENTS: {p.components}
MECHANICAL: {p.mechanical_design}
Return structured dimensions, placements, clearances, joints, mounting, center_of_mass assumptions and export specification. {extra or ''}"""
    def apply(self,p,r):
        p.cad_specification=r.get("data",r)
        return p
