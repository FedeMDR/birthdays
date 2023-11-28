import requests

res = requests.get("https://api.openaq.org/v2/locations/2178", headers={"X-API-Key": "my-openaq-api-key-12345-6789"})
