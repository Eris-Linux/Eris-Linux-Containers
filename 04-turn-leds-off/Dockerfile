#
# Dockerfile for the `turn-leds-off` Eris Linux container
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

# Install the `turn-leds-off` shell script.
#
COPY turn-leds-off.sh /turn-leds-off.sh
RUN chmod +x /turn-leds-off.sh

# Run the script.
#
CMD ["/turn-leds-off.sh"]
