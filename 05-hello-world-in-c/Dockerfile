#
# Dockerfile for the `hello-world-in-c` Eris Linux container
#
# Christophe BLAESS 2026
#
# License MIT
#

# This Dockerfile consists of two parts:
# - first, instructions for compiling into a dedicated container the excutable from the source code,
# - and second, instructions for creating the final container, which will contain only the executable.
#

################### Build container #########################################
#
# Use an Alpine Linux base image as build container.
#
# For reproducible builds, you may prefer a fixed version such as
# `alpine:3.22` instead of the latest one.
#
FROM  alpine:latest AS build

# Install the packages necessary to build a C program.
#
RUN apk add --no-cache build-base file

# Install the `hello-world-in-c` source file and the `Makefile`.
#
WORKDIR /src
COPY hello-world-in-c.c Makefile .

# Build the executable
#
RUN make


################### Final container #########################################
#
# Use an Alpine Linux base image as final container.
#
# For reproducible builds, you may prefer a fixed version such as
# `alpine:3.22` instead of the latest one.
#
FROM alpine:latest

# Install the executable and run it at container load.
#
COPY --from=build /src/hello-world-in-c /hello-world-in-c

CMD ["/hello-world-in-c"]

