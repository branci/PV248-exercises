# PV248 Python, Group 2
# Part 5 - Serving HTTP
# Branislav Smik
# 30.10.2017


import http.server


PORT = 8000

class MyHttpServer(http.server.BaseHTTPRequestHandler):

    def do_GET(self):
        self.protocol_version = 'HTTP/1.0'
        self.send_response( 200, 'OK' )
        self.send_header('Content-Type', 'text/plain' )
        self.end_headers()

        if self.path == '/':
            self.wfile.write(bytes("Welcome to the awesome server!\n", 'UTF-8'))
        elif self.path == "/file.txt":
            self.wfile.write(bytes("You requested " + self.path[1:] + " and I humbly accept the request.", 'UTF-8'))
        else:
            self.wfile.write(bytes("404 - Page not found\n", 'UTF-8'))


def main():
    print("serving at port", PORT)
    my_server = http.server.HTTPServer(('', PORT), MyHttpServer)
    my_server.serve_forever()

if __name__ == "__main__":
    main()