#
# Dockerfile for the `hello-world-in-python` Eris Linux container.
#
# Author: ChatGPT 2026.
#
# License: MIT
#

ARG ALPINE_VERSION=3.22

# ==============================================================================
# Certificate generation stage
# ==============================================================================

# Generate a self-signed TLS certificate.
#
# This certificate is sufficient for a demonstration HTTPS service, but it should
# not be used as-is for production deployments.
#
FROM --platform=$BUILDPLATFORM alpine:${ALPINE_VERSION} AS certificates

RUN apk add --no-cache openssl

RUN mkdir -p /out \
 && openssl req                                                   \
      -x509                                                       \
      -newkey rsa:2048                                            \
      -nodes                                                      \
      -keyout /out/hello-world.key                                \
      -out /out/hello-world.crt                                   \
      -days 3650                                                  \
      -subj "/CN=eris-linux-python-hello-world"                   \
 && chmod 600 /out/hello-world.key


# ==============================================================================
# Final container
# ==============================================================================

# Use an Alpine Linux base image.
#
# For reproducible builds, you may prefer a fixed version such as
# `alpine:3.22` instead of the latest one.
#
FROM alpine:${ALPINE_VERSION}

# Install Python 3.
#
RUN apk add --no-cache python3

# Install the HTTPS certificate and private key.
#
COPY --from=certificates /out/hello-world.crt /etc/eris-linux/ssl/hello-world.crt
COPY --from=certificates /out/hello-world.key /etc/eris-linux/ssl/hello-world.key

# Install the Python application.
#
COPY hello-world-in-python.py /hello-world-in-python.py
RUN chmod +x /hello-world-in-python.py

# Document that the container listens on TCP port 443.
#
# Note that the port is actually made reachable from outside the container
# by the container configuration, for example:
# Device Manager -> `My containers` -> `Setup` -> `Exported Ports` -> `443:443/tcp`
#
EXPOSE 443

# Run Python in unbuffered mode so that console messages are immediately visible.
#
CMD [ "python3", "-u", "/hello-world-in-python.py" ]
