import os
from http.server import SimpleHTTPRequestHandler, HTTPServer

host = 'localhost'
port = 8080

class MyHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        requested_path = self.path.lstrip('/')

	# validate results, do not allow requests to unauthorized locations
        try:
            validated_path = self.validate_path(requested_path)
        except ValueError as e:
            self.send_response(403)
            self.wfile.write(f"Error: {str(e)}".encode('utf-8'))
            return

        if os.path.isfile(validated_path):
            self.send_response(200)
            self.wfile.write(open(validated_path, 'rb').read())
        else:
            self.send_response(404)
            self.wfile.write(b"file not found")
    
    def validate_path(self, user_input):
        full_path = os.path.normpath(os.path.join(os.getcwd(), user_input))

        if not full_path.startswith(os.getcwd()):
            raise ValueError("invalid input: path trav detected")
        
        return full_path

server_address = (host, port)
httpd = HTTPServer(server_address, MyHandler)

print(f"Serving HTTP on {host} port {port}...")

try:
    httpd.serve_forever()
except KeyboardInterrupt:
    print("shutting server down")
    httpd.server_close()

