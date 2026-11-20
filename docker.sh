#!/bin/sh
if ! groups | grep docker; then
    echo "$USER is not in docker group"
    sudo gpasswd -a $USER docker
    echo "relogin and execute script again"
    exit 
fi
cd "$(dirname "$0")"
if [ ! -f .env ]; then 
    echo ".env file created.\n"
    echo " \
    DJANGO_KEY=$(openssl rand -hex 64)\n \
    POSTGRES_PASS=$(openssl rand -hex 64)\n \
    POSTGRES_NAME=$USER\n \
    POSTGRES_USER=$USER\n \
    " >> .env
fi
docker compose up --build