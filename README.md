Quantum Secure Email Client 🔐✉️
This project is a Post-Quantum Cryptography (PQC) based secure email client built with Python. It demonstrates how modern encryption techniques—resistant to quantum attacks—can be integrated into typical email workflows using simulated Kyber-like encapsulation, symmetric encryption, and Gmail integration with App Passwords.

📌 Features
🔐 Post-Quantum Key Encapsulation using simulated Kyber1024 logic.

🔑 Symmetric AES-GCM encryption for message confidentiality.

📩 Email encryption and sending via Gmail SMTP (App Password-based).

📥 Decryption and reading of received secure emails via IMAP.

🛡️ Email credentials stored securely in a local CSV file (demo only).

🧪 Ready-to-run examples for both sending and receiving encrypted emails.

📁 Folder Structure
bash
Copy
Edit
quantum_secure_email_client/
├── crypto/
│   ├── pqcrypto.py
│   └── symmetric.py
├── email_client/
│   ├── sender.py
│   ├── receiver.py
│   └── key_utils.py
├── keys/
│   ├── sender_private_key.pem
│   └── receiver_public_key.pem
├── email_client/senders.csv
├── keygen_receiver.py
├── .gitignore
└── README.md
🔧 Setup Instructions
1. Clone the repository
bash
Copy
Edit
git clone https://github.com/your-username/quantum-secure-email-client.git
cd quantum_secure_email_client
2. Install required packages
bash
Copy
Edit
pip install -r requirements.txt
⚠️ If requirements.txt doesn't exist, manually install:
pip install cryptography

3. Generate Receiver Key Pair
bash
Copy
Edit
python keygen_receiver.py
This generates a receiver’s key pair and saves it to the keys/ directory.

✉️ Sending a Secure Email
bash
Copy
Edit
python email_client/sender.py
You’ll be prompted to enter:

A sender email address (must exist in email_client/senders.csv with its app password).

A receiver email address (must have a public key already generated).

A plaintext message.

The script:

Loads the receiver's public key.

Encapsulates a shared secret.

Encrypts the message with AES-GCM.

Sends the ciphertext via Gmail SMTP.

📬 Receiving & Decrypting the Email
bash
Copy
Edit
python email_client/receiver.py
This script:

Logs into the receiver’s Gmail via IMAP.

Scans for unread messages with a specific subject.

Extracts the ciphertext and decrypts the message using the private key.

Displays the original message.

🔐 Gmail App Password Configuration
Since Gmail blocks access from less secure apps:

Enable 2-Step Verification in your Google Account.

Go to App Passwords

Generate a new app password.

Store the email and app password in email_client/senders.csv.

Example format (senders.csv):

csv
Copy
Edit
email,password
alice123@gmail.com,app_password_here
bob456@gmail.com,another_app_password

📚 What is Post-Quantum Cryptography?
Post-Quantum Cryptography (PQC) refers to cryptographic algorithms designed to resist attacks from quantum computers. This project simulates such techniques (like Kyber) to show how secure communications might work in a post-quantum era.

📌 Future Improvements
Replace simulated PQ logic with real implementations (e.g., via pqcrypto or pyca/cryptography with PQ support).

Add GUI using Tkinter or PyQt.

Integrate secure storage (e.g., using a keyring manager or encrypted vault for credentials).

🧑‍💻 Author
Manga567
GitHub: @Manga567
