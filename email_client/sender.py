import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import smtplib
from email.message import EmailMessage
from crypmangto import pqcrypto, symmetric
from cryptography.fernet import Fernet
import base64
import hashlib

def load_receiver_public_key(receiver_email):
    try:
        with open("keys/receiver_public_key.pem", "rb") as f:
            public_key = f.read()
        print("🔑 Loading recipient's public key...")
        return public_key
    except FileNotFoundError:
        print("❌ Public key for the recipient not found.")
        exit(1)

def derive_fernet_key(shared_secret):
    if isinstance(shared_secret, str):
        shared_secret = shared_secret.encode()
    digest = hashlib.sha256(shared_secret).digest()
    return base64.urlsafe_b64encode(digest)

def encrypt(plaintext, shared_secret):
    key = derive_fernet_key(shared_secret)
    f = Fernet(key)
    return f.encrypt(plaintext.encode()).decode()

def send_secure_email(sender_email, sender_password, receiver_email, plaintext):
    print("🔐 Generating shared secret using PQ encryption...")
    public_key = load_receiver_public_key(receiver_email)
    ciphertext, shared_secret = pqcrypto.encapsulate(public_key)

    print("📤 Simulating encapsulation of shared secret...")

    print("🧪 Encrypting the email body...")
    encrypted_body = encrypt(plaintext, shared_secret)

    msg = EmailMessage()
    msg["Subject"] = "Quantum Encrypted Email"
    msg["From"] = sender_email
    msg["To"] = receiver_email

    # Use the actual ciphertext (hex) and encrypted body, separated by a blank line
    if isinstance(ciphertext, bytes):
        ciphertext_str = ciphertext.hex()
    else:
        ciphertext_str = str(ciphertext)
    msg.set_content(f"{ciphertext_str}\n\n{encrypted_body}")

    print("📨 Connecting to SMTP server...")
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()

    print(f"📡 Attempting login...\nEmail: {sender_email}\nPassword: {sender_password}")

    server.login(sender_email, sender_password)
    server.send_message(msg)
    server.quit()
    print("✅ Email sent successfully.")

# --- Execution starts here ---

sender_email = "quantumcryp3@gmail.com"
sender_password = "ilcnnmdrvohcvzqz"
receiver_email = input("Enter receiver email: ").strip()
message = input("Enter your message: ").strip()

send_secure_email(sender_email, sender_password, receiver_email, message)