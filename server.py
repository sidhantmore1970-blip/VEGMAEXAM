"""
Vagmi Exim Website — Python Server
Run: python server.py
Then open: http://localhost:8000
"""
 
from http.server import HTTPServer, SimpleHTTPRequestHandler
import os
 
PORT = 8000
DIRECTORY = os.path.dirname(os.path.abspath(__file__))
 
class Handler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)
 
    def log_message(self, format, *args):
        print(f"[Vagmi Exim] {self.address_string()} - {format % args}")
 
if __name__ == "__main__":
    server = HTTPServer(("0.0.0.0", PORT), Handler)
    print(f"\n✅ Vagmi Exim website running at http://localhost:{PORT}\n")
    print("Press Ctrl+C to stop.\n")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nServer stopped.")
 