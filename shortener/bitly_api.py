import requests
from django.conf import settings


def shorten_url(long_url):
    headers = {
        "Authorization": f"Bearer {settings.BITLY_ACCESS_TOKEN}",
        "Content-Type": "application/json",
    }
    json_data = {"long_url": long_url}
    response = requests.post(
        "https://api-ssl.bitly.com/v4/shorten", json=json_data, headers=headers
    )
    if response.status_code in [200, 201]:
        return response.json().get("link")
    else:
        print(f"Bitly API error: {response.status_code} - {response.text}")
        return None
