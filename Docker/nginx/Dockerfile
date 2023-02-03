FROM nginx:latest

RUN rm /etc/nginx/conf.d/default.conf
COPY /Docker/nginx/nginx.conf /Docker/nginx/.htpasswd /etc/nginx/conf.d/
