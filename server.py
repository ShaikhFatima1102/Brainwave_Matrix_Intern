from http.server import BaseHTTPRequestHandler, HTTPServer
import json

class RequestHandler(BaseHTTPRequestHandler):
    def do_OPTIONS(self):
        """Handle CORS preflight requests."""
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.end_headers()

    def do_POST(self):
        """Handle POST requests."""
        if self.path == '/check_url':
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length).decode('utf-8')
            data = json.loads(post_data)
            url = data.get('url', '')

            # Dummy phishing check logic
            keywords = [
    "phishing", "scam", "fraud", "malware", "spyware", "trojan", "hacker",
    "ransomware", "keylogger", "phish", "impersonate", "exploit", "virus",
    "bypass", "compromised", "credential", "suspicious", "malicious", 
    "attack", "threat", "spam", "fake", "deceptive", "untrusted", 
    "rogue", "intrusion", "socialengineering", "baits", "spoof"
]

            is_phishing = any(keyword in url for keyword in keywords)

            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
            response = {'is_phishing': is_phishing}
            self.wfile.write(json.dumps(response).encode('utf-8'))
        else:
            self.send_error(404, 'Not Found')

PORT = 8000

def run(server_class=HTTPServer, handler_class=RequestHandler):
    server_address = ('', PORT)
    httpd = server_class(server_address, handler_class)
    print(f'Starting server on port {PORT}...')
    httpd.serve_forever()

if __name__ == "__main__":
    run()