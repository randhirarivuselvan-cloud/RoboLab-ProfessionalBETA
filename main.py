from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from api.routes import router

app = FastAPI(
    title="RoboLab Universal Professional",
    description="Universal AI robotics engineering platform by SynapseX Robotics & Technologies",
    version="4.0.0",
)
app.include_router(router, prefix="/api")

web_static = Path("web/static")
if web_static.exists():
    app.mount("/static", StaticFiles(directory=str(web_static)), name="static")

@app.get("/", include_in_schema=False)
def frontend():
    return FileResponse("web/index.html")

@app.get("/health", tags=["system"])
def health():
    return {"status": "ok", "service": "RoboLab", "version": "4.0.0"}
