import requests

def lookup(ip):
    url = f"https://ipinfo.io/{ip}/json"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        print(f"IP: {data.get('ip')}")
        print(f"Location: {data.get('city')}, {data.get('region')}, {data.get('country')}")
        print(f"Org: {data.get('org')}")
        print(f"Location: {data.get('loc')}")
    else:
        print("Error retrieving IP info.")