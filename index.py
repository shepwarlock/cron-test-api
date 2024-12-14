from bs4 import BeautifulSoup
from http.server import BaseHTTPRequestHandler
import requests

x = "test"
z = "yes"

url = "https://www.example.com"
response = requests.get(url)
html_content = response.content

soup = BeautifulSoup(html_content, 'html.parser')

# Extract the title of the page
title = soup.title.string

# Find all the links on the page
links = soup.find_all('a')
for link in links:
    z = link.get('href')


class handler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type','text/plain')
        self.end_headers()
        self.wfile.write(f'z={z}'.encode('utf-8'))
        self.wfile.write(f'Hello, {x}!'.encode('utf-8'))
        return
