from __future__ import annotations
import json, sqlite3
from pathlib import Path
from core.models import Project, ProjectCreate

DB = Path("data/robolab.db")
DB.parent.mkdir(parents=True, exist_ok=True)

class Database:
    def __init__(self):
        self.init()
    def conn(self):
        c = sqlite3.connect(DB)
        c.row_factory = sqlite3.Row
        return c
    def init(self):
        with self.conn() as c:
            c.execute("CREATE TABLE IF NOT EXISTS projects (project_id TEXT PRIMARY KEY, data TEXT NOT NULL, updated_at TEXT NOT NULL)")
            c.execute("CREATE TABLE IF NOT EXISTS ai_runs (id INTEGER PRIMARY KEY AUTOINCREMENT, project_id TEXT, stage TEXT, status TEXT, created_at TEXT DEFAULT CURRENT_TIMESTAMP)")
            c.commit()
    def create_project(self, payload: ProjectCreate):
        p = Project(name=payload.name, metadata={"idea": payload.idea, "requirements_input": payload.requirements})
        p.user_requirements = payload.requirements or [payload.idea]
        self.save_project(p)
        return p
    def save_project(self, p: Project):
        p.touch()
        with self.conn() as c:
            c.execute("INSERT OR REPLACE INTO projects(project_id,data,updated_at) VALUES(?,?,?)",
                      (p.project_id, p.model_dump_json(), p.updated_at))
            c.commit()
        return p
    def get_project(self, project_id):
        with self.conn() as c:
            row = c.execute("SELECT data FROM projects WHERE project_id=?", (project_id,)).fetchone()
        return Project.model_validate_json(row["data"]) if row else None

db = Database()
