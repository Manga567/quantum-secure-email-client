import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Fetch values
EMAIL_ADDRESS = os.getenv("EMAIL_ADDRESS")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")

# Server info
SMTP_SERVER = "smtp.gmail.com"
IMAP_SERVER = "imap.gmail.com"

if __name__ == "__main__":
    print("EMAIL_ADDRESS:", EMAIL_ADDRESS)
    print("EMAIL_PASSWORD:", EMAIL_PASSWORD)
    print("SMTP_SERVER:", SMTP_SERVER)
    print("IMAP_SERVER:", IMAP_SERVER)
