import requests

def search(username):
    platforms = [
        f"https://www.instagram.com/{username}",
        f"https://twitter.com/{username}",
        f"https://www.facebook.com/{username}",
        f"https://www.linkedin.com/in/{username}"
    ]
    for platform in platforms:
        response = requests.get(platform)
        if response.status_code == 200:
            print(f"Found {username} on {platform}")
        else:
            print(f"{username} not found on {platform}")