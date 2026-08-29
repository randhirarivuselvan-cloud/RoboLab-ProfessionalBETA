from core.models import Project
from services.validation import validate_cross_stage

def test_pin_conflict():
    p=Project(user_requirements=["test"],pin_map=[{"pin":25,"signal":"motor_a"},{"pin":25,"signal":"motor_b"}])
    issues=validate_cross_stage(p)
    assert any("Pin conflict" in x for x in issues)
