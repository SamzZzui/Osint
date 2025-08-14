import requests

def search(phone_number):
    url = f"https://api.phoneinfoga.com/lookup?number={phone_number}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        print(f"Phone Number: {data.get('number')}")
        print(f"Location: {data.get('location')}")
        print(f"Carrier: {data.get('carrier')}")
    else:
        print("Error retrieving phone number info.")