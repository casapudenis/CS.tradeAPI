import requests
import json

response_API = requests.get('https://cdn.cs.trade:2096/api/prices_CSGO')
if response_API.status_code == 200:
    data = response_API.json()
    items = []
    prices = []
    for item in data:
        price = data[item]['price']
        if price > 150:
            items.append(item)
            prices.append(price)
    for i in range(len(items)):
        print(f"{items[i]}: {prices[i]}")
else:
    print("Failed to retrieve data from API.")