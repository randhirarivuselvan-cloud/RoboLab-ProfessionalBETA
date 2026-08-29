from ai.agents.builder import BuilderAgent
from ai.agents.circuit import CircuitAgent
from ai.agents.code import CodeAgent
from ai.agents.cad import CADAgent
from ai.agents.verification import VerificationAgent
from ai.agents.compiler import CompilerAgent
from ai.agents.auditor import AuditorAgent

AGENTS = {
    "builder": BuilderAgent(),
    "circuit": CircuitAgent(),
    "code": CodeAgent(),
    "cad": CADAgent(),
    "verify": VerificationAgent(),
    "compile": CompilerAgent(),
    "audit": AuditorAgent(),
}
