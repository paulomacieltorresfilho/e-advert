import os, dotenv

dotenv.load_dotenv()

email_password = os.getenv('EMAIL_PASSWORD')
print(email_password)
