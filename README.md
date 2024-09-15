# PhishingDetection


Phishing Link Detection Server
Phishing Link Detection Server is a Python-based HTTP server designed to identify potentially malicious URLs using keyword matching. The server listens for HTTP requests and checks URLs against a predefined list of keywords commonly associated with phishing and other types of cyber threats.

How It Works
Server Setup:

The server is implemented using Python’s built-in http.server module.
It starts on port 8000 and listens for incoming HTTP requests.
CORS Support:

The server handles CORS (Cross-Origin Resource Sharing) preflight requests to allow web applications hosted on different domains to interact with it.
This is done in the do_OPTIONS method, which responds to preflight OPTIONS requests with appropriate CORS headers.
Handling POST Requests:

When a POST request is made to the /check_url endpoint, the server processes the request to check the provided URL.
The request body must be a JSON object containing a single field url, which holds the URL to be checked.
Phishing Detection Logic:

Upon receiving the URL, the server reads the data and extracts the URL from the JSON payload.
It then checks if the URL contains any keywords from a predefined list that are indicative of phishing or malicious intent.
The list of keywords includes terms such as "phishing", "scam", "fraud", "malware", and others commonly associated with cyber threats.
Response:

Based on the keyword matching, the server determines whether the URL is considered potentially phishing.
It sends back a JSON response with a single field is_phishing set to true if any keyword is found in the URL, otherwise false.
Error Handling:

If a request is made to an undefined endpoint, the server responds with a 404 Not Found error
