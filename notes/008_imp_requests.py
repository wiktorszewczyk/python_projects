import requests

link = "https://wikipedia.org/"

website_raw = requests.get(link)
website_text = website_raw.text

print(website_text)
