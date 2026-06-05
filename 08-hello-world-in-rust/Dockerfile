#
# Dockerfile for the `hello-world-in-rust` Eris Linux container
#
# Alexandre GROSSET 2026
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

# Install the packages necessary to build a Rust program.
#
RUN apk add --no-cache build-base file rust cargo

# Install the `hello-world-in-rust` source file and the `Cargo.toml` file.
#
WORKDIR /src
COPY  .  .

# Build the executable
#
RUN cargo build  --release


################### Final container #########################################
#
# Use an Alpine Linux base image as final container.
#
# For reproducible builds, you may prefer a fixed version such as
# `alpine:3.22` instead of the latest one.
#
FROM alpine:latest

# Install the runtime needed package.
#
RUN apk add --no-cache libgcc

# Install the executable and run it at container load.
#
COPY --from=build /src/target/release/example-hello-world /example-hello-world
CMD ["/example-hello-world"]

