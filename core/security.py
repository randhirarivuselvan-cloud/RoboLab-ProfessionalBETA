import hashlib, hmac
def constant_time_equal(a: str, b: str) -> bool:
    return hmac.compare_digest(a, b)
def hash_identifier(value: str) -> str:
    return hashlib.sha256(value.encode()).hexdigest()
