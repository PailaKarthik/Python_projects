

import requests
import json
query=input("enter the topic you want : ")
url=f"https://newsapi.org/v2/everything?q={query}&from=2023-04-23&sortBy=publishedAt&apiKey=1223d6c399724b48b8a48ada4f7a378e"
r=requests.get(url)
news=json.loads(r.text)
for article in news["articles"]:
    print(article["title"])
    print(article["description"])
    print("----------------------------------------------------")