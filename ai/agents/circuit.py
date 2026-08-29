from ai.base import Agent
class CircuitAgent(Agent):
    stage="circuit"
    system_prompt="""You are RoboLab Circuit AI, a universally professional electrical/electronics engineering generator.
You MUST consume the canonical architecture and components. Detect pin conflicts, voltage mismatches, incompatible interfaces,
missing power requirements and impossible connections. Never independently invent hardware that contradicts the canonical design."""
    def model(self): return None
    def build_prompt(self,p,extra=None):
        return f"""Generate/refine the electrical architecture.
CANONICAL ARCHITECTURE: {p.architecture}
COMPONENTS: {p.components}
CURRENT PIN MAP: {p.pin_map}
POWER: {p.power_budget}
Return JSON with components, connections, pin_map, power_budget, warnings. {extra or ''}"""
    def apply(self,p,r):
        d=r.get("data",r)
        for k in ("components","connections","pin_map","power_budget"):
            if k in d: setattr(p,k,d[k])
        p.warnings.extend(d.get("warnings",[]))
        return p
