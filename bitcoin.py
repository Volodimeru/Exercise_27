import requests
import sys

if len(sys.argv) < 2 :
    sys.exit("Muissing command-line argument")
elif len(sys.argv) > 2:
    sys.exit("Too many command-line argument")
elif not sys.argv[1].isdigit():
    sys.exit("Command-line argument is not a number")
elif int(sys.argv[1]) <=0:
    sys.exit("Command-line argument is not a positive number ")
else:
    try:
        resp = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
        o = resp.json()
        z = float(sys.argv[1]) * float(o["bpi"]["USD"]["rate_float"])
        print(f"${z:,.4f}")
    except requests.RequestException:
       print("RequestException")
       sys.exit()