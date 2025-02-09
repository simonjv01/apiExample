import requests
import json

response = requests.get('https://api.nasa.gov/insight_weather/?api_key=DEMO_KEY&feedtype=json&ver=1.0')

data = response.json()

print(json.dumps(data, indent=4))
