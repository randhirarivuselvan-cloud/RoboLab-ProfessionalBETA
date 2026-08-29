from ai.base import Agent
class CodeAgent(Agent):
    stage="code"
    system_prompt="""You are RoboLab Code AI, a universally professional firmware/software engineering generator.
You MUST consume the canonical architecture and circuit specification. Never invent independent hardware connections.
Respect selected controller, actual pins, sensors, actuators, buses, protocols, startup/shutdown and error handling."""
    def model(self): return None
    def build_prompt(self,p,extra=None):
        return f"""Generate/refine firmware/control software.
CONTROLLER/ARCHITECTURE: {p.architecture}
COMPONENTS: {p.components}
CONNECTIONS: {p.connections}
PIN MAP: {p.pin_map}
Return JSON with target, dependencies, firmware_source, control_logic, error_handling, startup_shutdown, referenced_pins. {extra or ''}"""
    def apply(self,p,r):
        d=r.get("data",r)
        p.firmware=d
        return p
