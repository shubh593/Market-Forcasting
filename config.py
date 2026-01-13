import os
from dotenv import load_dotenv

load_dotenv()

DELTA_API_KEY = os.getenv("DELTA_API_KEY")

BASE_URL = "https://api.delta.exchange"
