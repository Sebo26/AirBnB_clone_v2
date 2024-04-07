#!/usr/bin/env bash
# sets up your web servers for the deployment of web_static
sudo apt-get update
sudo apt-get install -y nginx
mkdir -p "/data/"
mkdir -p "/data/web_static/"
mkdir -p "/data/web_static/releases/"
mkdir -p "/data/web_static/shared/"
mkdir -p "/data/web_static/releases/test/"
touch "/data/web_static/releases/test/index.html"
ln -sf "/data/web_static/current" "/data/web_static/releases/test/"
chown -R ubuntu:ubuntu "/data/"
tee /etc/nginx/sites-available/web_static <<EOF
server {
	location hbnb_static {
	alias /data/web_static/current/;
}
EOF
sudo service nginx reload
