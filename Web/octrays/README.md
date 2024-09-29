# Oct Rays

MacOS .DS_Store shows a file listing

Creator - [@PlatyPew](https://github.com/PlatyPew)

## Category

Web

## Question

> State-of-the-art compilers for the LOW-price of half your life savings! What are you waiting for? Give me your money!
>
> Connect via http://<ip address>:30003/

### Hint

- The directory was uploaded from macOS

## Setup Guide

`docker compose up -d octrays`

## Distribution

None given

## Solution

Use a directory scanner to find that there is a `.DS_Store` file.

Download it and view the directory contents.

Use Python `ds_store` module to see the list of files.

```python
from ds_store import DSStore
with DSStore.open("DS_Store") as ds:
    for item in ds:
            print(item)

```

```text
<alpha20_cf9e67 b'Iloc'>
<app.py b'Iloc'>
<index.html b'Iloc'>
<pricing.html b'Iloc'>
```

Access `/alpha20_cf9e67` and get the flag from `flag.txt`.

### Flag

`CyberBlitz{rip_to_whoever_who_did_not_gitignore_the_dsstore_file}`
