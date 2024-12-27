FROM nginx:latest

RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    fcgiwrap \
    spawn-fcgi && \
    apt-get clean

COPY nginx.conf /etc/nginx/nginx.conf
COPY fastcgi /usr/local/fastcgi
COPY fastcgi/fcgiwrap.service /etc/systemd/system/fcgiwrap.service

RUN systemctl enable fcgiwrap.service

EXPOSE 80
