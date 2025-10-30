"""
Webhook endpoint for Vercel serverless function
Receives POST requests from Dayforce and stores data
"""

from flask import Flask, request, jsonify, make_response
from functools import wraps
from datetime import datetime
import json
import os

app = Flask(__name__)

# Get credentials from environment variables
USERNAME = os.getenv('WEBHOOK_USERNAME', 'dayforce')
PASSWORD = os.getenv('WEBHOOK_PASSWORD', 'envalior2025')

# In-memory storage (Vercel serverless - data persists per instance)
received_data = []

def check_auth(username, password):
    """Check if a username/password combination is valid."""
    return username == USERNAME and password == PASSWORD

def authenticate():
    """Sends a 401 response that enables basic auth"""
    return make_response(
        jsonify({'error': 'Authentication required'}), 
        401,
        {'WWW-Authenticate': 'Basic realm="Login Required"'}
    )

def requires_auth(f):
    """Decorator to require basic authentication"""
    @wraps(f)
    def decorated(*args, **kwargs):
        auth = request.authorization
        if not auth or not check_auth(auth.username, auth.password):
            return authenticate()
        return f(*args, **kwargs)
    return decorated

@app.route('/')
def index():
    """Main page"""
    return jsonify({
        'status': 'online',
        'service': 'Dayforce Webhook Receiver',
        'version': '1.0.0',
        'endpoints': {
            'webhook': '/webhook (POST - requires Basic Auth)',
            'data': '/data (GET)',
            'latest': '/latest (GET)',
            'test': '/test (GET/POST)'
        },
        'authentication': {
            'type': 'Basic Auth',
            'username': USERNAME
        }
    })

@app.route('/webhook', methods=['POST'])
@requires_auth
def webhook():
    """Main webhook endpoint to receive POST data"""
    
    # Get timestamp
    timestamp = datetime.now().isoformat()
    
    # Get POST data
    if request.is_json:
        data = request.get_json()
    else:
        data = request.form.to_dict() or request.data.decode('utf-8')
    
    # Store data
    entry = {
        'timestamp': timestamp,
        'headers': dict(request.headers),
        'data': data,
        'method': request.method,
        'url': request.url,
        'remote_addr': request.remote_addr
    }
    
    received_data.append(entry)
    
    # Keep only last 100 entries
    if len(received_data) > 100:
        received_data.pop(0)
    
    # Log to Vercel
    print(f"[{timestamp}] Webhook received from {request.remote_addr}")
    print(f"Data: {json.dumps(data, indent=2)}")
    
    # Send response
    return jsonify({
        'status': 'success',
        'message': 'Data received successfully',
        'timestamp': timestamp,
        'received_data': data
    }), 200

@app.route('/data', methods=['GET'])
def get_all_data():
    """View all received POST data"""
    return jsonify({
        'total_requests': len(received_data),
        'data': received_data
    })

@app.route('/latest', methods=['GET'])
def get_latest():
    """View latest POST data"""
    if received_data:
        return jsonify(received_data[-1])
    else:
        return jsonify({'message': 'No data received yet'}), 404

@app.route('/test', methods=['GET', 'POST'])
def test():
    """Test endpoint"""
    return jsonify({
        'status': 'ok',
        'message': 'Test endpoint working',
        'method': request.method,
        'timestamp': datetime.now().isoformat(),
        'authenticated': request.authorization is not None,
        'data': request.get_json() if request.is_json else None
    })

# For local testing
if __name__ == '__main__':
    print("="*60)
    print("Webhook Server Starting (Local Mode)")
    print("="*60)
    print(f"Username: {USERNAME}")
    print(f"Password: {PASSWORD}")
    print("="*60)
    app.run(host='0.0.0.0', port=5000, debug=True)
