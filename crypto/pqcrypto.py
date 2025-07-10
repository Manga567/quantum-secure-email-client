import os

def generate_keypair():
    print("🔐 Simulating Kyber1024 keypair generation...")
    public_key = b"SimulatedPublicKey_123456"
    private_key = b"SimulatedPrivateKey_123456"
    return public_key, private_key, "Kyber1024"

def encapsulate(public_key):
    print("📤 Simulating encapsulation of shared secret...")
    ciphertext = os.urandom(32)  # 32 random bytes as ciphertext
    shared_secret = ciphertext  # Use ciphertext as shared secret for demo
    return ciphertext, shared_secret

def decapsulate(ciphertext, private_key):
    print("📥 Simulating decapsulation...")
    shared_secret = ciphertext  # Use ciphertext as shared secret for demo
    return shared_secret