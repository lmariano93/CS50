import sys
import requests
import json

def main():

    if len(sys.argv) == 2:
        try:
            n = float(sys.argv[1])
        except ValueError:
            print("Command-line argument is not a valid number")
            sys.exit(1)
    else:
        print("Missing command-line argument")
        sys.exit(1)

    try:
        req = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
        req.raise_for_status()
        data = req.json()
        usd = float(data["bpi"]["USD"]["rate_float"])
        amount = usd * n
        print(f"${amount:,.4f}")
    except requests.RequestException as e:
        print(f"Error fetching data from CoinDesk API: {e}")
        sys.exit(1)


main()
