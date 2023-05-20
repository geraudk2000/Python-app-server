from http.server import HTTPServer, BaseHTTPRequestHandler

HOST = '0.0.0.0'
PORT = 8080

class Handler(BaseHTTPRequestHandler):
    

    def do_GET(self):
       self.send_response(200)
       self.send_header('Content-Type', 'text/plain')
       self.end_headers()

       message = 'Hello World!' 