import requests

def lookup(image_path):
    url = "https://api.tineye.com/rest/search/"
    files = {'image': open(image_path, 'rb')}
    response = requests.post(url, files=files)
    if response.status_code == 200:
        data = response.json()
        if data['results']:
            for result in data['results']:
                print(f"Found image at: {result['url']}")
        else:
            print("No matches found.")
    else:
        print("Error performing image search.")