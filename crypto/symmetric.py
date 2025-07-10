from cryptography.fernet import Fernet
import base64
import hashlib

def derive_fernet_key(shared_secret: bytes) -> bytes:
    """
    Derives a Fernet-compatible 32-byte base64 key from the shared secret.
    """
    key = hashlib.sha256(shared_secret).digest()
    return base64.urlsafe_b64encode(key)

def encrypt_message(message: str, shared_secret: bytes) -> str:
    """
    Encrypts the message using Fernet (AES under the hood).
    Returns a base64-encoded string.
    """
    key = derive_fernet_key(shared_secret)
    f = Fernet(key)
    encrypted = f.encrypt(message.encode())
    return encrypted.decode()  # Return as string for email

def decrypt_message(encrypted_message: str, shared_secret: bytes) -> str:
    """
    Decrypts the message using Fernet.
    Accepts a base64-encoded string.
    """
    key = derive_fernet_key(shared_secret)
    f = Fernet(key)
    decrypted = f.decrypt(encrypted_message.encode())
    return decrypted.decode()

# 🔧 Test the module independently
if __name__ == "__main__":
    dummy_secret = b"this_is_32_byte_shared_secret!!__"[:32]
    msg = "Quantum secure email: Hello World!"
    encrypted = encrypt_message(msg, dummy_secret)
    print(f"🔒 Encrypted: {encrypted}")

    decrypted = decrypt_message(encrypted, dummy_secret)
    print(f"🔓 Decrypted: {decrypted}")