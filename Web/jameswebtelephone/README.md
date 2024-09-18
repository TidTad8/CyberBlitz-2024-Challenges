# James Web Telephone

Using a hash length extension attack to bypass the signature checks

Creator - [@PlatyPew](https://github.com/PlatyPew)

## Category

Web

## Question

> This is the last time I get an intern to design my web application!
> ~ NASA Probably
>
> Connect via http://<ip address>:30002/

### Hint

None given

## Setup Guide

`docker compose up -d jameswebtelephone`

## Distribution

-   app.py: `5f1108b5e148dab867a17c5f9ab3380eb45887fc68fb6ccdc72ee636686211cd`

## Solution

A classic hash length extension attack.

Instead of using a HMAC, it uses this.

```python
validate_signature = hashlib.sha256(SECRET + header + data).digest()
```

This allows us to add on to the append data and calculate the new hash without knowing what `SECRET` is.

You can use hashpump to generate the new hash.
All we have to do is to first generate the initial token and extract out each field.
Next, append `name:b"name:administrator;` and recalculate the hash.
Update the JWT and send a GET request to the `/api/flag` endpoint.

### Flag

`CyberBlitz{YOU_THOUGHT_IT_WAS_A_WEB_CHALLENGE_BUT_IT_WAS_I_CRYPTO}`
