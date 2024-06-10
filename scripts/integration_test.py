import os
import requests


ID_TOKEN = os.environ.get("ID_TOKEN")
URL = os.environ.get("SERVICE_URL")


res = requests.get(
    url=f"{URL}/",
    headers={
        "Authorization": f"Bearer {ID_TOKEN}"
    }
)

if res.status_code == 200:
    print(res.json())
    exit(0)
else:
    print(res.text)
    exit(1)