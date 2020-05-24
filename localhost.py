import http.server
import socketserver
import ourdb

PORT = 8080
Handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("serving at port", PORT)
    ourdb.initDatabase()
    httpd.serve_forever()