import os

NOTION_TOKEN = os.environ["NOTION_TOKEN"]

BOOK_LOG_DATABASE_ID = os.environ["NOTION_DATABASE_ID"]
QUOTES_DATABASE_ID = os.environ["NOTION_QUOTES_DATABASE_ID"]


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