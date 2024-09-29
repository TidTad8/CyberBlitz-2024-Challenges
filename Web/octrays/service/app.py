import http.server
import socketserver


class GetFile(http.server.SimpleHTTPRequestHandler):

    def do_GET(self):
        if self.path == "/":
            self.path = "/index.html"

        super().do_GET()


def run_server(port: int = 8000):
    handler = GetFile
    socketserver.ThreadingTCPServer.allow_reuse_address = True
    with socketserver.ThreadingTCPServer(("", port), handler) as httpd:
        print(f"Serving at port {port}")
        httpd.serve_forever()


if __name__ == "__main__":
    run_server()
