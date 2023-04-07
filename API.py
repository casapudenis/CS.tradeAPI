import requests
import json
response_API = requests.get('https://cdn.cs.trade:2096/api/prices_CSGO')
print(response_API.status_code)
data = response_API.text
parse_json=json.loads(data)
with open('output_file.json', 'w') as f:
    json.dump(parse_json, f)


