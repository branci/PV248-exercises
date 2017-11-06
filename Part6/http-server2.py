# PV248 Python, Group 2
# Part 5 - Serving HTTP
# Branislav Smik
# 30.10.2017

# returns a JSON/HTML page with scores for a composer specified in the URL parameter
# (functionality from the search.py file)
# open in a browser: http://localhost:8000/result?q=Bach%20j%20s&f=html
# params q=Your search string
# params f=html/json

import http.server
import urllib.parse as urlparse
import sqlite3
import json
from search2 import composers_scores

DATABASE = "scorelib_rockai_final.dat"
PORT = 8000

class MyHttpServer(http.server.BaseHTTPRequestHandler):

    def do_GET(self):
        #connect to a DB to fulfill GET requests
        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()

        self.protocol_version = 'HTTP/1.0'
        self.send_response( 200, 'OK' )

        url_query = urlparse.urlparse(self.path).query
        url_dict = urlparse.parse_qs(url_query)
        #print("query string: ", url_dict)

        if url_dict.get('f')[0] == 'json':
            #set plaintext header
            self.send_header('Content-Type', 'text/plain')
            self.end_headers()

            self.wfile.write(bytes("JSON for search query = {}:\n\n".format(url_dict.get('q')[0]), 'UTF-8'))
            db_result = composers_scores(cursor, url_dict.get('q')[0])
            self.wfile.write(bytes(db_result, 'UTF-8'))
        elif url_dict.get('f')[0] == 'html':
            #set HTML header
            self.send_header('Content-Type', 'text/html')
            self.end_headers()

            #print HTML
            self.wfile.write(bytes("<html><head><title>Search composers</title></head>", 'UTF-8'))
            self.wfile.write(bytes("<p>HTML for search query = <b><i>{}</i></b></p>".format(url_dict.get('q')[0]), 'UTF-8'))

            db_result = json.loads(composers_scores(cursor, url_dict.get('q')[0]))
            for key, value in db_result.items():
                self.wfile.write(bytes(str("<h4>%s</h4>" % (key,)), 'UTF-8'))
                for v in value:
                    self.wfile.write(bytes(str("<li>%s</li>" % (v,)), 'UTF-8'))
        else:
            self.wfile.write(bytes("404 - Page not found\n", 'UTF-8'))


def main():
    print("serving at port", PORT)
    my_server = http.server.HTTPServer(('', PORT), MyHttpServer)
    my_server.serve_forever()

if __name__ == "__main__":
    main()