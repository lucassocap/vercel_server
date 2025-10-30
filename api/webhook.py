"""""""""

Vercel Serverless Webhook Handler

Simple Python HTTP handler - no Flask dependencySimple webhook receiver for Vercel serverlessWebhook endpoint for Vercel serverless function

"""

No Flask - pure Python HTTP handlerReceives POST requests from Dayforce and stores data

from http.server import BaseHTTPRequestHandler

import json""""""

import os

from datetime import datetime

import base64

from http.server import BaseHTTPRequestHandlerfrom flask import Flask, request, jsonify, make_response

# Credentials from environment

USERNAME = os.getenv('WEBHOOK_USERNAME', 'dayforce')from urllib.parse import urlparse, parse_qsfrom functools import wraps

PASSWORD = os.getenv('WEBHOOK_PASSWORD', 'envalior2025')

import jsonfrom datetime import datetime

# In-memory storage (last 100 requests)

received_data = []import osimport json



def check_auth(auth_header):from datetime import datetimeimport os

    """Validate Basic Authentication"""

    if not auth_header:import base64

        return False

    try:app = Flask(__name__)

        auth_type, credentials = auth_header.split(' ', 1)

        if auth_type.lower() != 'basic':# Get credentials from environment variables

            return False

        decoded = base64.b64decode(credentials).decode('utf-8')USERNAME = os.getenv('WEBHOOK_USERNAME', 'dayforce')# Get credentials from environment variables

        username, password = decoded.split(':', 1)

        return username == USERNAME and password == PASSWORDPASSWORD = os.getenv('WEBHOOK_PASSWORD', 'envalior2025')USERNAME = os.getenv('WEBHOOK_USERNAME', 'dayforce')

    except:

        return FalsePASSWORD = os.getenv('WEBHOOK_PASSWORD', 'envalior2025')



class handler(BaseHTTPRequestHandler):# In-memory storage

    

    def do_GET(self):received_data = []# In-memory storage (Vercel serverless - data persists per instance)

        """Handle GET requests"""

        if self.path in ['/', '/api', '/api/']:received_data = []

            self.json_response({

                'status': 'online',def check_auth(auth_header):

                'service': 'Dayforce Webhook Receiver',

                'endpoints': {    """Check Basic Authentication"""def check_auth(username, password):

                    'webhook': '/api/webhook (POST)',

                    'data': '/api/data (GET)',    if not auth_header:    """Check if a username/password combination is valid."""

                    'latest': '/api/latest (GET)',

                    'test': '/api/test (GET/POST)'        return False    return username == USERNAME and password == PASSWORD

                }

            })    

        

        elif self.path == '/api/test':    try:def authenticate():

            self.json_response({

                'status': 'ok',        auth_type, credentials = auth_header.split(' ', 1)    """Sends a 401 response that enables basic auth"""

                'method': 'GET',

                'timestamp': datetime.now().isoformat()        if auth_type.lower() != 'basic':    return make_response(

            })

                    return False        jsonify({'error': 'Authentication required'}), 

        elif self.path == '/api/data':

            self.json_response({                401,

                'total': len(received_data),

                'data': received_data        decoded = base64.b64decode(credentials).decode('utf-8')        {'WWW-Authenticate': 'Basic realm="Login Required"'}

            })

                username, password = decoded.split(':', 1)    )

        elif self.path == '/api/latest':

            if received_data:        return username == USERNAME and password == PASSWORD

                self.json_response(received_data[-1])

            else:    except:def requires_auth(f):

                self.json_response({'message': 'No data'}, 404)

                return False    """Decorator to require basic authentication"""

        else:

            self.json_response({'error': 'Not found'}, 404)    @wraps(f)

    

    def do_POST(self):class handler(BaseHTTPRequestHandler):    def decorated(*args, **kwargs):

        """Handle POST requests"""

        if self.path == '/api/webhook':    def do_GET(self):        auth = request.authorization

            # Check auth

            if not check_auth(self.headers.get('Authorization')):        """Handle GET requests"""        if not auth or not check_auth(auth.username, auth.password):

                self.send_response(401)

                self.send_header('WWW-Authenticate', 'Basic realm="Login"')        path = self.path            return authenticate()

                self.send_header('Content-Type', 'application/json')

                self.end_headers()                return f(*args, **kwargs)

                self.wfile.write(json.dumps({'error': 'Auth required'}).encode())

                return        if path == '/' or path == '/api' or path == '/api/':    return decorated

            

            # Get data            self.send_json_response({

            length = int(self.headers.get('Content-Length', 0))

            body = self.rfile.read(length).decode('utf-8') if length > 0 else '{}'                'status': 'online',@app.route('/')

            

            try:                'service': 'Dayforce Webhook Receiver',def index():

                data = json.loads(body)

            except:                'version': '1.0.0',    """Main page"""

                data = body

                            'endpoints': {    return jsonify({

            # Store

            timestamp = datetime.now().isoformat()                    'webhook': '/api/webhook (POST - requires Basic Auth)',        'status': 'online',

            received_data.append({

                'timestamp': timestamp,                    'data': '/api/data (GET)',        'service': 'Dayforce Webhook Receiver',

                'data': data

            })                    'latest': '/api/latest (GET)',        'version': '1.0.0',

            

            # Keep last 100                    'test': '/api/test (GET/POST)'        'endpoints': {

            if len(received_data) > 100:

                received_data.pop(0)                },            'webhook': '/webhook (POST - requires Basic Auth)',

            

            self.json_response({                'authentication': {            'data': '/data (GET)',

                'status': 'success',

                'timestamp': timestamp                    'type': 'Basic Auth',            'latest': '/latest (GET)',

            })

                            'username': USERNAME            'test': '/test (GET/POST)'

        elif self.path == '/api/test':

            self.json_response({                }        },

                'status': 'ok',

                'method': 'POST',            })        'authentication': {

                'timestamp': datetime.now().isoformat()

            })                    'type': 'Basic Auth',

        

        else:        elif path == '/api/test':            'username': USERNAME

            self.json_response({'error': 'Not found'}, 404)

                self.send_json_response({        }

    def json_response(self, data, status=200):

        """Send JSON response"""                'status': 'ok',    })

        self.send_response(status)

        self.send_header('Content-Type', 'application/json')                'message': 'Test endpoint working',

        self.end_headers()

        self.wfile.write(json.dumps(data).encode())                'method': 'GET',@app.route('/webhook', methods=['POST'])


                'timestamp': datetime.now().isoformat()@requires_auth

            })def webhook():

            """Main webhook endpoint to receive POST data"""

        elif path == '/api/data':    

            self.send_json_response({    # Get timestamp

                'total_requests': len(received_data),    timestamp = datetime.now().isoformat()

                'data': received_data    

            })    # Get POST data

            if request.is_json:

        elif path == '/api/latest':        data = request.get_json()

            if received_data:    else:

                self.send_json_response(received_data[-1])        data = request.form.to_dict() or request.data.decode('utf-8')

            else:    

                self.send_json_response({'message': 'No data received yet'}, status=404)    # Store data

            entry = {

        else:        'timestamp': timestamp,

            self.send_error(404, "Not Found")        'headers': dict(request.headers),

            'data': data,

    def do_POST(self):        'method': request.method,

        """Handle POST requests"""        'url': request.url,

        path = self.path        'remote_addr': request.remote_addr

            }

        if path == '/api/test':    

            content_length = int(self.headers.get('Content-Length', 0))    received_data.append(entry)

            body = self.rfile.read(content_length).decode('utf-8') if content_length > 0 else '{}'    

                # Keep only last 100 entries

            try:    if len(received_data) > 100:

                data = json.loads(body) if body else {}        received_data.pop(0)

            except:    

                data = None    # Log to Vercel

                print(f"[{timestamp}] Webhook received from {request.remote_addr}")

            self.send_json_response({    print(f"Data: {json.dumps(data, indent=2)}")

                'status': 'ok',    

                'message': 'Test endpoint working',    # Send response

                'method': 'POST',    return jsonify({

                'timestamp': datetime.now().isoformat(),        'status': 'success',

                'data': data        'message': 'Data received successfully',

            })        'timestamp': timestamp,

                'received_data': data

        elif path == '/api/webhook':    }), 200

            # Check authentication

            auth_header = self.headers.get('Authorization')@app.route('/data', methods=['GET'])

            if not check_auth(auth_header):def get_all_data():

                self.send_response(401)    """View all received POST data"""

                self.send_header('WWW-Authenticate', 'Basic realm="Login Required"')    return jsonify({

                self.send_header('Content-Type', 'application/json')        'total_requests': len(received_data),

                self.end_headers()        'data': received_data

                self.wfile.write(json.dumps({'error': 'Authentication required'}).encode())    })

                return

            @app.route('/latest', methods=['GET'])

            # Get POST datadef get_latest():

            content_length = int(self.headers.get('Content-Length', 0))    """View latest POST data"""

            body = self.rfile.read(content_length).decode('utf-8') if content_length > 0 else '{}'    if received_data:

                    return jsonify(received_data[-1])

            try:    else:

                data = json.loads(body)        return jsonify({'message': 'No data received yet'}), 404

            except:

                data = body@app.route('/test', methods=['GET', 'POST'])

            def test():

            # Store data    """Test endpoint"""

            timestamp = datetime.now().isoformat()    return jsonify({

            entry = {        'status': 'ok',

                'timestamp': timestamp,        'message': 'Test endpoint working',

                'headers': dict(self.headers),        'method': request.method,

                'data': data,        'timestamp': datetime.now().isoformat(),

                'method': 'POST'        'authenticated': request.authorization is not None,

            }        'data': request.get_json() if request.is_json else None

                })

            received_data.append(entry)

            # For local testing

            # Keep only last 100if __name__ == '__main__':

            if len(received_data) > 100:    print("="*60)

                received_data.pop(0)    print("Webhook Server Starting (Local Mode)")

                print("="*60)

            self.send_json_response({    print(f"Username: {USERNAME}")

                'status': 'success',    print(f"Password: {PASSWORD}")

                'message': 'Data received successfully',    print("="*60)

                'timestamp': timestamp,    app.run(host='0.0.0.0', port=5000, debug=True)

                'received_data': data
            })
        
        else:
            self.send_error(404, "Not Found")
    
    def send_json_response(self, data, status=200):
        """Send JSON response"""
        self.send_response(status)
        self.send_header('Content-Type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()
        self.wfile.write(json.dumps(data, indent=2).encode())
