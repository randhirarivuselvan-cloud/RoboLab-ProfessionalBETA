import os, json, httpx
from ai.base import AIProvider
class AnthropicProvider(AIProvider):
    name="anthropic"
    def available(self): return bool(os.getenv("AI_API_KEY"))
    def generate(self, system, prompt, model=None):
        key=os.getenv("AI_API_KEY",""); model=model or os.getenv("AI_MODEL")
        if not model: return {"status":"failed","error_code":"AI_MODEL_NOT_CONFIGURED","message":"AI_MODEL is required.","recoverable":True}
        try:
            r=httpx.post("https://api.anthropic.com/v1/messages",headers={"x-api-key":key,"anthropic-version":"2023-06-01","content-type":"application/json"},
                         json={"model":model,"max_tokens":8000,"system":system,"messages":[{"role":"user","content":prompt}]},timeout=90)
            r.raise_for_status(); text="".join(x.get("text","") for x in r.json().get("content",[]))
            return {"status":"passed","data":json.loads(text)}
        except Exception as e:
            return {"status":"failed","error_code":"AI_REQUEST_FAILED","message":str(e),"recoverable":True}
