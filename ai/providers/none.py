from ai.base import AIProvider
class NoneProvider(AIProvider):
    name="none"
    def available(self): return False
    def generate(self, system, prompt, model=None):
        return {"status":"failed","error_code":"AI_PROVIDER_NOT_CONFIGURED","message":"No AI provider configured.","recoverable":True}
