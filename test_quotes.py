import requests

from notion import HEADERS, QUOTES_DATABASE_URL


response = requests.post(
    QUOTES_DATABASE_URL,
    headers=HEADERS,
    json={
        "page_size": 1
    }
)

print(response.status_code)
print(response.text)