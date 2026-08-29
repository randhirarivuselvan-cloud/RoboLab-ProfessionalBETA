from fastapi import APIRouter, HTTPException
from core.models import ProjectCreate, Project, StageRunRequest
from core.database import db
from ai.orchestrator import orchestrator

router = APIRouter()

@router.get("/status")
def status():
    return {"status": "ok", "service": "RoboLab API", "version": "4.0.0"}

@router.post("/projects", response_model=Project)
def create_project(payload: ProjectCreate):
    return db.create_project(payload)

@router.get("/projects/{project_id}", response_model=Project)
def get_project(project_id: str):
    project = db.get_project(project_id)
    if not project:
        raise HTTPException(404, "Project not found")
    return project

@router.post("/projects/{project_id}/{stage}")
def run_stage(project_id: str, stage: str, request: StageRunRequest | None = None):
    project = db.get_project(project_id)
    if not project:
        raise HTTPException(404, "Project not found")
    result = orchestrator.run_stage(project, stage, request.prompt if request else None)
    db.save_project(result)
    return result

@router.get("/projects/{project_id}/export")
def export_project(project_id: str):
    project = db.get_project(project_id)
    if not project:
        raise HTTPException(404, "Project not found")
    from services.exports import export_project_zip
    path = export_project_zip(project)
    return {"status": "ready", "file": str(path)}

@router.get("/ai/providers")
def providers():
    return orchestrator.provider_status()
