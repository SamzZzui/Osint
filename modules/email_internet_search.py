import requests

def search(email):
    url = f"https://api.emailrep.io/{email}"
    headers = {"User-Agent": "YourAppName"}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        print(f"Email: {data.get('email')}")
        print(f"Reputation: {data.get('reputation')}")
        print(f"First Seen: {data.get('first_seen')}")
        print(f"Last Seen: {data.get('last_seen')}")
    else:
        print("Error retrieving email information.")