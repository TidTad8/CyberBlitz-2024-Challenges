import http.server
import socketserver

class MyHttpRequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.path = 'main.html'
        elif self.path == '/botty':
            self.path = 'botty.html'
        return http.server.SimpleHTTPRequestHandler.do_GET(self)

PORT = 8000
handler_object = MyHttpRequestHandler

my_server = socketserver.TCPServer(("", PORT), handler_object)
print("Server started at localhost:" + str(PORT))
my_server.serve_forever()