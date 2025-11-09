import os
from dotenv import load_dotenv

load_dotenv()

REDIS_URL = os.getenv("REDIS_URL", "redis://localhost:6379/0")
DATABASE_PATH = os.getenv("DATABASE_PATH", "scraped_data.sqlite3")
TARGET_URL = os.getenv("TARGET_URL", "http://quotes.toscrape.com/js/")
HEADLESS = os.getenv("HEADLESS", "true").lower() in ("1", "true", "yes")
