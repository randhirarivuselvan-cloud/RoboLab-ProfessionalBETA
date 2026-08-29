from fastapi.testclient import TestClient
from main import app

client=TestClient(app)

def test_api_status():
    r=client.get("/api/status")
    assert r.status_code==200
    assert r.json()["status"]=="ok"

def test_frontend_route():
    r=client.get("/")
    assert r.status_code==200
    assert "RoboLab" in r.text

def test_project_creation_and_retrieval():
    r=client.post("/api/projects",json={"name":"Test Robot","idea":"A wheeled robot","requirements":["move"]})
    assert r.status_code==200
    pid=r.json()["project_id"]
    r2=client.get(f"/api/projects/{pid}")
    assert r2.status_code==200
    assert r2.json()["project_id"]==pid

def test_unconfigured_ai_is_honest():
    r=client.get("/api/ai/providers")
    assert r.status_code==200
    assert r.json()["available"] is False
