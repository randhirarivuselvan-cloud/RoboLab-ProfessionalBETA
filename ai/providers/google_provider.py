import os, json, httpx
from ai.base import AIProvider
class GoogleProvider(AIProvider):
    name="google"
    def available(self): return bool(os.getenv("AI_API_KEY"))
    def generate(self, system, prompt, model=None):
        key=os.getenv("AI_API_KEY",""); model=model or os.getenv("AI_MODEL")
        if not model: return {"status":"failed","error_code":"AI_MODEL_NOT_CONFIGURED","message":"AI_MODEL is required.","recoverable":True}
        url=f"https://generativelanguage.googleapis.com/v1beta/models/{model}:generateContent?key={key}"
        try:
            r=httpx.post(url,json={"system_instruction":{"parts":[{"text":system}]},"contents":[{"parts":[{"text":prompt}]}]},timeout=90)
            r.raise_for_status(); text=r.json()["candidates"][0]["content"]["parts"][0]["text"]
            text=re_strip(text)
            return {"status":"passed","data":json.loads(text)}
        except Exception as e:
            return {"status":"failed","error_code":"AI_REQUEST_FAILED","message":str(e),"recoverable":True}
def re_strip(text):
    if "```" in text:
        text=text.replace("```json","").replace("```","")
    return text.strip()
