#!/usr/bin/env python3
#
# Simple Python HTTPS "Hello World" example for Eris Linux containers.
#
# ChatGPT 2026
#
# License: MIT
#

import ssl
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer


HOST = "0.0.0.0"
PORT = 443

CERT_FILE = "/etc/eris-linux/ssl/hello-world.crt"
KEY_FILE = "/etc/eris-linux/ssl/hello-world.key"


class HelloWorldHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        print("Hello World", flush=True)

        body = b"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <title>Eris Linux Python container</title>
</head>
<body>
  <h1>Hello World</h1>
  <p>This page is served by a Python HTTPS server running in an Eris Linux container.</p>
</body>
</html>
"""

        self.send_response(200)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def log_message(self, fmt, *args):
        print("%s - %s" % (self.address_string(), fmt % args), flush=True)


def main():
    print("Hello World (from Python)", flush=True)
    print(f"Starting HTTPS server on port {PORT}", flush=True)

    server = ThreadingHTTPServer((HOST, PORT), HelloWorldHandler)

    context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
    context.load_cert_chain(certfile=CERT_FILE, keyfile=KEY_FILE)

    server.socket = context.wrap_socket(server.socket, server_side=True)

    server.serve_forever()


if __name__ == "__main__":
    main()

