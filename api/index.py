import requests
from http.server import BaseHTTPRequestHandler
 
class handler(BaseHTTPRequestHandler):
 
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type','text/plain')
        self.end_headers()
        self.wfile.write('Hello, world!'.encode('utf-8'))
        return   # api/hello.py
   def handler(request, event):
       return {
           "statusCode": 200,
           "body": "Hello from Python!"
       }
