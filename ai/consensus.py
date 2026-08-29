from core.models import Project

def consensus(project: Project):
    findings = project.verification_results
    failures = [f for f in findings if f.get("severity") == "failure"]
    if failures or project.errors:
        project.status = "REVISE"
        project.audit_results = {"decision":"REVISE","reasons":failures or project.errors}
    else:
        project.status = "PASS"
        project.audit_results = {"decision":"PASS","note":"Consensus passed the currently available verification results; appropriate engineering validation is still required."}
    return project
