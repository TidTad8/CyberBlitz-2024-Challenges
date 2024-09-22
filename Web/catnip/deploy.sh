#!/bin/sh

# Last tested on Debian

docker compose up --build -d
sleep 20
docker exec -it catnip-ctf-catnip_api-1 python manage.py migrate
