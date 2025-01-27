import requests

def get_api_data(endpoint):
    response = requests.get(f"http://example.com{endpoint}")
    response.raise_for_status()
    return response.json()
