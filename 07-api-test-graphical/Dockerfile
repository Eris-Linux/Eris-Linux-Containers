#
# Dockerfile for the `api-test-tcp` Eris Linux container
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
FROM alpine:latest AS build

# Install the packages necessary to build a C program.
# (curl-dev is needed by liberis, pkgconf and libstdc++ by Qt).
#
RUN apk add --no-cache build-base file curl-dev libstdc++ pkgconf qt6-qtbase-dev git ca-certificates

WORKDIR /src

# Download the source files of the `liberis` library.
#
ARG LIBERIS_REPO=https://github.com/Eris-Linux/liberis.git
ARG LIBERIS_BRANCH=master
RUN git clone --depth 1 --branch "${LIBERIS_BRANCH}" "${LIBERIS_REPO}" /src/liberis

# Build liberis as a static library.
# So we won't need to install it in the final container.
#
WORKDIR /src/liberis
RUN make static
RUN make static_install
WORKDIR /src

# Copy the application sources, headers, Makefile and qss file.
#
COPY sources/* .

# Build the application.
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

# Install the libcurl (needed by liberis).
#
RUN apk add --no-cache libcurl

# Install Qt libraries
#
RUN apk add --no-cache qt6-qtbase-x11 qt6-qtdeclarative fontconfig  ttf-dejavu

# Install the executable and run it at container load.
#
COPY --from=build /src/graphic-api-test /graphic-api-test
COPY --from=build /src/api-test.qss /api-test.qss

CMD ["/graphic-api-test"]
