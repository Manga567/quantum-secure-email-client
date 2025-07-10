# key_utils.py

def save_key(path: str, key_bytes: bytes):
    with open(path, 'wb') as f:
        f.write(key_bytes)

def load_key(path: str) -> bytes:
    with open(path, 'rb') as f:
        return f.read()
