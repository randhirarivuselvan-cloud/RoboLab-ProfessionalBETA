from pathlib import Path
import json, zipfile, tempfile, shutil

def export_project_zip(project):
    out=Path(tempfile.gettempdir())/f"RoboLab_Project_{project.project_id}.zip"
    with zipfile.ZipFile(out,"w",zipfile.ZIP_DEFLATED) as z:
        z.writestr("README.md", "# RoboLab Engineering Project\n\nRequires appropriate engineering validation and human review.\n")
        z.writestr("project.json", project.model_dump_json(indent=2))
        z.writestr("architecture.json", json.dumps(project.architecture,indent=2))
        z.writestr("components.json", json.dumps(project.components,indent=2))
        z.writestr("wiring.json", json.dumps({"connections":project.connections,"pin_map":project.pin_map,"power_budget":project.power_budget},indent=2))
        z.writestr("firmware.json", json.dumps(project.firmware,indent=2))
        z.writestr("cad_specification.json", json.dumps(project.cad_specification,indent=2))
        z.writestr("analysis_report.json", json.dumps(project.simulation_results,indent=2))
        z.writestr("verification_report.json", json.dumps(project.verification_results,indent=2))
        z.writestr("final_audit_report.json", json.dumps(project.audit_results,indent=2))
    return out
