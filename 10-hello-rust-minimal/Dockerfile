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
# Use a Rust distro to build the code.
#
FROM rust:1.96.0 AS builder

# Install the `hello-world-in-rust` source file and the `Cargo.toml` file.
#
WORKDIR /app
COPY  .  .

# Build the executable statically.
#
ARG FULLARCH
RUN rustup target add "${FULLARCH}"
RUN cargo build  --target "${FULLARCH}" --release


################### Final container #########################################
#
# Use an empty Docker containing only the executable.
#
FROM scratch
ARG FULLARCH
COPY --from=builder /app/target/${FULLARCH}/release/example-hello-world /example-hello-world
EXPOSE 3000
CMD ["/example-hello-world"]
