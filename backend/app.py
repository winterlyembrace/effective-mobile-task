from http.server import HTTPServer, BaseHTTPRequestHandler

class MyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        # Health check endpoint for liveness/readiness probes
        if self.path == '/health':
            self.send_response(200)
            self.send_header('Content-type', 'text/plain; charset=utf-8')
            self.end_headers()
            self.wfile.write("OK".encode('utf-8'))

        # Main application endpoint
        elif self.path == '/':
            self.send_response(200)
            self.send_header('Content-type', 'text/plain; charset=utf-8')
            self.end_headers()
            response = "Hello from Effective Mobile!"
            self.wfile.write(response.encode('utf-8'))

        # Return 404 for any other undefined paths
        else:
            self.send_response(404)
            self.send_header('Content-type', 'text/plain; charset=utf-8')
            self.end_headers()
            self.wfile.write("404 Not Found".encode('utf-8'))

# Server configuration
server_address = ('', 8080)
httpd = HTTPServer(server_address, MyHandler)

print("Server started at http://localhost:8080")
httpd.serve_forever()
