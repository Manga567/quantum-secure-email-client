import os

# Simulated key pair
receiver_public_key = b"SIMULATED_RECEIVER_PUBLIC_KEY"
receiver_private_key = b"SIMULATED_RECEIVER_PRIVATE_KEY"

# Make sure the keys folder exists
os.makedirs("keys", exist_ok=True)

# Save public key
with open("keys/receiver_public_key.pem", "wb") as f:
    f.write(receiver_public_key)

# Save private key
with open("keys/receiver_private_key.pem", "wb") as f:
    f.write(receiver_private_key)

print("✅ Receiver key pair generated and saved in 'keys/' directory.")
