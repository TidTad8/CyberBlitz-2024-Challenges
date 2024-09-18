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

```bash
python3 parse.py .DS_Store
```

```text
alpha20_cf9e67
        Icon location: x 67px, y 44px, 0xffffffffffff0000
app.py
        Icon location: x 186px, y 60px, 0xffffffffffff0000
index.html
        Icon location: x 285px, y 46px, 0xffffffffffff0000
pricing.html
        Icon location: x 388px, y 51px, 0xffffffffffff0000
```

Access `/alpha20_cf9e67` and get the flag.

### Flag

`CyberBlitz{rip_to_whoever_who_did_not_gitignore_the_dsstore_file}`
