import os, json, httpx
from ai.base import AIProvider
class LocalProvider(AIProvider):
    name="local"
    def available(self): return bool(os.getenv("LOCAL_AI_URL"))
    def generate(self, system, prompt, model=None):
        try:
            r=httpx.post(os.getenv("LOCAL_AI_URL"),json={"model":model or os.getenv("AI_MODEL","local"),"system":system,"prompt":prompt},timeout=120)
            r.raise_for_status()
            data=r.json()
            return {"status":"passed","data":data.get("data",data)}
        except Exception as e:
            return {"status":"failed","error_code":"LOCAL_AI_REQUEST_FAILED","message":str(e),"recoverable":True}
