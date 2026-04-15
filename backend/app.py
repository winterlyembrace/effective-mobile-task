from http.server import HTTPServer, BaseHTTPRequestHandler

class MyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        
        self.send_header('Content-type', 'text/html; charset=utf-8')
        self.end_headers()
        
        response = "<h1>Hello from Effective Mobile!</h1>"
        self.wfile.write(response.encode('utf-8'))

server_address = ('', 8080)
httpd = HTTPServer(server_address, MyHandler)

httpd.serve_forever()
