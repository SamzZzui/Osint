import requests

def search(name, email=None):
    url = f"https://api.peopledb.com/search?name={name}"
    if email:
        url += f"&email={email}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        if data:
            for person in data:
                print(f"Name: {person['name']}")
                print(f"Email: {person['email']}")
                print(f"Phone: {person['phone']}")
                print(f"Address: {person['address']}")
        else:
            print("No results found.")
    else:
        print("Error retrieving people search results.")