import requests

def search(email):
    url = f"https://haveibeenpwned.com/api/v3/breachedaccount/{email}"
    headers = {"User-Agent": "YourAppName"}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        breaches = response.json()
        print(f"Breaches found for {email}:")
        for breach in breaches:
            print(f"- {breach['Name']} ({breach['Domain']})")
    elif response.status_code == 404:
        print(f"No breaches found for {email}.")
    else:
        print("Error checking email breaches.")