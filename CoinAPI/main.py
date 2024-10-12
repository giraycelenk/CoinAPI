from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json

url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
parameters = {

}
headers = {
  'Accepts': 'application/json',
  'X-CMC_PRO_API_KEY': 'API key will be written here.',
}

session = Session()
session.headers.update(headers)

try:
    response = session.get(url, params=parameters)
    data = json.loads(response.text)
    for item in data["data"]:
        if item["id"] == 1 or item["id"] == 1027:
            name = item["name"]
            price = item["quote"]["USD"]["price"]
            print(f"{name} PRICE: {price}")

except (ConnectionError, Timeout, TooManyRedirects) as e:
    print(e)