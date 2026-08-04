import requests

from notion import HEADERS


url = "https://api.notion.com/v1/search"


response = requests.post(
    url,
    headers=HEADERS,
    json={
        "query": "FRASES_"
    }
)

response.raise_for_status()

data = response.json()


for result in data["results"]:
    print("\n----------------")
    print("ID:", result["id"])
    print("Tipo:", result["object"])

    if result["object"] == "database":
        print("Título:", result["title"][0]["plain_text"])