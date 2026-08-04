import os

NOTION_TOKEN = os.environ["NOTION_TOKEN"]

BOOK_LOG_DATABASE_ID = "2fe25802a031808090f2dc7178eacc54"

QUOTES_DATABASE_ID = "30b25802a03180ee931cf31e2e2fb773"


HEADERS = {
    "Authorization": f"Bearer {NOTION_TOKEN}",
    "Content-Type": "application/json",
    "Notion-Version": "2022-06-28"
}


BOOK_LOG_DATABASE_URL = (
    f"https://api.notion.com/v1/databases/{BOOK_LOG_DATABASE_ID}/query"
)


QUOTES_DATABASE_URL = (
    f"https://api.notion.com/v1/databases/{QUOTES_DATABASE_ID}/query"
)