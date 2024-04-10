import requests
url = "https://www.cursoemvideo.com/"

try:
    print(requests.get("https://www.cursoemvideo.com/").status_code)
except Exception as e:
    print(f"Sistema Indisponível.")
