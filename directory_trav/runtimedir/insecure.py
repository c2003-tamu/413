import os
from http.server import SimpleHTTPRequestHandler, HTTPServer

host = 'localhost'
port = 8080

class MyHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        file_path = self.path.lstrip('/')
	
	# simply serve file if exists without santizing results
        if os.path.isfile(file_path):
            self.send_response(200)
            self.wfile.write(open(file_path, 'rb').read())
        else:
            self.send_response(404)
            self.wfile.write(b"file not found")


server_address = (host, port)
httpd = HTTPServer(server_address, MyHandler)

print(f"Serving HTTP on {host} port {port}...")

try:
    httpd.serve_forever()
except KeyboardInterrupt:
    print("shutting server down")
    httpd.server_close()



