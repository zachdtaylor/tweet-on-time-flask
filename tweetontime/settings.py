from dotenv import load_dotenv
from pathlib import Path
import os

load_dotenv()

BASE_DIR = Path(__file__).resolve(strict=True).parent.parent

BEARER_TOKEN = os.getenv("BEARER_TOKEN")
API_KEY = os.getenv("API_KEY")
API_SECRET_KEY = os.getenv("API_SECRET_KEY")
ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")
ACCESS_TOKEN_SECRET = os.getenv("ACCESS_TOKEN_SECRET")

SECRET_KEY = os.getenv("SECRET_KEY")

DATABASE = {
    'PATH': BASE_DIR / 'instance' / 'tweetontime.sqlite'
}
