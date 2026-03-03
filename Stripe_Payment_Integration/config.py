from dotenv import load_dotenv
import os

load_dotenv()

class Settings:
    STRIPE_SECRET_KEY: str = os.getenv("STRIPE_SECRET_KEY")
    STRIPE_WEBHOOK_SECRET: str = os.getenv("STRIPE_WEBHOOK_SECRET")
    DATABASE_URL: str = os.getenv("DATABASE_URL")

settings = Settings()