import requests
from config import BASE_URL, DELTA_API_KEY

def get_market_data(symbol="BTCUSDT"):
    url = f"{BASE_URL}/v2/tickers/{symbol}"

    headers = {
        "Authorization": f"Bearer {DELTA_API_KEY}"
    }

    response = requests.get(url, headers=headers)
    response.raise_for_status()

    return response.json()
