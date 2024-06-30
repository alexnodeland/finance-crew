import json
import requests
from openai import OpenAI

def validate_openai_key(api_key):
    client = OpenAI(api_key=api_key)
    try:
        client.models.list()
        return True
    except:
        return False

def validate_serper_key(api_key):
    url = "https://google.serper.dev/search"
    payload = json.dumps({"q": "test"})
    headers = {
        'X-API-KEY': api_key,
        'Content-Type': 'application/json'
    }
    try:
        response = requests.request("POST", url, headers=headers, data=payload)
        return response.status_code == 200
    except:
        return False