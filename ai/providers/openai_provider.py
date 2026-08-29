import os, json, httpx
from ai.base import AIProvider
class OpenAIProvider(AIProvider):
    name="openai"
    def available(self): return bool(os.getenv("AI_API_KEY"))
    def generate(self, system, prompt, model=None):
        key=os.getenv("AI_API_KEY",""); model=model or os.getenv("AI_MODEL")
        if not model: return {"status":"failed","error_code":"AI_MODEL_NOT_CONFIGURED","message":"AI_MODEL is required.","recoverable":True}
        base=os.getenv("AI_BASE_URL","https://api.openai.com/v1").rstrip("/")
        try:
            r=httpx.post(base+"/chat/completions",headers={"Authorization":f"Bearer {key}","Content-Type":"application/json"},
                         json={"model":model,"messages":[{"role":"system","content":system},{"role":"user","content":prompt}],"response_format":{"type":"json_object"}},timeout=90)
            r.raise_for_status(); content=r.json()["choices"][0]["message"]["content"]
            return {"status":"passed","data":json.loads(content)}
        except Exception as e:
            return {"status":"failed","error_code":"AI_REQUEST_FAILED","message":str(e),"recoverable":True}
