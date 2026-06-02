#
# Dockerfile for the `api-web-test-example` Eris Linux container
#
# Christophe BLAESS 2026
#
# License MIT
#

# Use an Alpine Linux base image.
# For reproducible builds, you may prefer a fixed version such as
# `alpine:3.22` instead of the latest one.
#
FROM alpine:latest

# Install the NginX package
#
RUN apk add --no-cache  nginx busybox-suid

# Install the content of the `frontend/` subdirectory.
#
COPY frontend/ /usr/share/nginx/html

# Install the customized NginX configuration file.
#
COPY deploy/nginx.conf /etc/nginx/http.d/default.conf

# Install the start script.
#
COPY deploy/start.sh /start.sh
RUN chmod +x /start.sh

# Document that the container listens on TCP port 80.
#
# Note that the port is actually made reachable from outside the
# container by the container configuration:
# Device Manager -> `My containers` -> `Setup` -> `Exported Ports` -> `22:22/tcp`
#
EXPOSE 80

# 
CMD ["/start.sh"]
