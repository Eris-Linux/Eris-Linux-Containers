#
# Dockerfile for the `ssh-server-example` Eris Linux container
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

# Install the OpenSSH package, generate the SSH host keys.
# Create an `eris` user and configure passwords for both `eris` and `root`.
#
RUN apk update                                                   \
 && apk add --no-cache openssh                                   \
 && ssh-keygen -A                                                \
 && echo "PermitRootLogin yes" >> /etc/ssh/sshd_config           \
 && echo "PasswordAuthentication yes" >> /etc/ssh/sshd_config    \
 && adduser -D eris                                              \
 && echo "root:root"  | chpasswd                                 \
 && echo "eris:linux" | chpasswd

# Document that the container listens on TCP port 22.
#
# Note that the port is actually made reachable from outside the
# container by the container configuration:
# Device Manager -> `My containers` -> `Setup` -> `Exported Ports` -> `22:22/tcp`
#
EXPOSE 22

# Start the OpenSSH server in the foreground so that it remains
# attached to the container's main process.
#
CMD [ "/usr/sbin/sshd", "-D" ]

