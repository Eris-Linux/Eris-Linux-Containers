#
# Dockerfile for the `leds-access-example` Eris Linux container
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

# Install the `led-trigger-setup` shell script.
#
COPY led-trigger-setup.sh /led-trigger-setup.sh
RUN chmod +x /led-trigger-setup.sh

# Run the script.
#
CMD ["/led-trigger-setup.sh"]
