import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
import base64
from crypto import pqcrypto, symmetric

def load_receiver_private_key():
    with open("keys/receiver_private_key.pem", "rb") as f:
        return f.read()

def parse_email_content(email_content):
    # Assumes the format: ciphertext\n\nencrypted_body
    parts = email_content.strip().split('\n\n', 1)
    if len(parts) != 2:
        raise ValueError("Invalid email format.")
    ciphertext_hex, encrypted_body = parts
    ciphertext = bytes.fromhex(ciphertext_hex)
    return ciphertext, encrypted_body

def decrypt_email(email_content):
    ciphertext, encrypted_body = parse_email_content(email_content)
    private_key = load_receiver_private_key()
    shared_secret = pqcrypto.decapsulate(ciphertext, private_key)
    decrypted_message = symmetric.decrypt_message(encrypted_body, shared_secret)
    return decrypted_message

if __name__ == "__main__":
    print("Paste the full email content (ciphertext and encrypted body), then press Ctrl+Z (Windows) or Ctrl+D (Linux/Mac) and Enter:")
    email_content = sys.stdin.read()
    print("DEBUG: Raw input received:")
    print(repr(email_content))

    try:
        decrypted = decrypt_email(email_content)
        print(f"\n🔓 Decrypted message:\n{decrypted}")
    except Exception as e:
        print(f"❌ Decryption failed: {e}")