"""
Test script for Vercel webhook endpoint
Tests the deployed webhook server at https://vercel-server-lyart-theta.vercel.app
"""

import requests
from requests.auth import HTTPBasicAuth
import json
from datetime import datetime
import urllib3

# Disable SSL warnings for corporate environment
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Vercel server URL
BASE_URL = "https://vercel-server-lyart-theta.vercel.app"
WEBHOOK_URL = f"{BASE_URL}/api/webhook"

# Credentials
USERNAME = "dayforce"
PASSWORD = "envalior2025"

def print_separator(title=""):
    """Print a separator line"""
    print("\n" + "="*60)
    if title:
        print(f"  {title}")
        print("="*60)

def test_root_endpoint():
    """Test the root endpoint"""
    print_separator("Testing Root Endpoint")
    
    try:
        response = requests.get(BASE_URL, verify=False, timeout=10)
        print(f"URL: {BASE_URL}")
        print(f"Status Code: {response.status_code}")
        
        if response.status_code == 200:
            print("✅ Root endpoint is working")
            print(f"Response: {json.dumps(response.json(), indent=2)}")
        else:
            print(f"❌ Unexpected status code: {response.status_code}")
            
        return response.status_code == 200
    except Exception as e:
        print(f"❌ Error: {str(e)}")
        return False

def test_webhook_without_auth():
    """Test webhook endpoint without authentication (should fail)"""
    print_separator("Testing Webhook WITHOUT Authentication")
    
    test_data = {
        "test": "webhook_no_auth",
        "timestamp": datetime.now().isoformat(),
        "message": "This should be rejected"
    }
    
    try:
        response = requests.post(
            WEBHOOK_URL,
            json=test_data,
            headers={"Content-Type": "application/json"},
            verify=False,
            timeout=10
        )
        
        print(f"URL: {WEBHOOK_URL}")
        print(f"Status Code: {response.status_code}")
        
        if response.status_code == 401:
            print("✅ Correctly rejected (401 Unauthorized)")
            return True
        else:
            print(f"❌ Should return 401, got {response.status_code}")
            return False
            
    except Exception as e:
        print(f"❌ Error: {str(e)}")
        return False

def test_webhook_with_auth():
    """Test webhook endpoint with authentication (should succeed)"""
    print_separator("Testing Webhook WITH Authentication")
    
    test_data = {
        "test": "webhook_with_auth",
        "timestamp": datetime.now().isoformat(),
        "message": "Test from Python script",
        "employee_id": "12345",
        "event_type": "employee.updated"
    }
    
    try:
        response = requests.post(
            WEBHOOK_URL,
            json=test_data,
            auth=HTTPBasicAuth(USERNAME, PASSWORD),
            headers={"Content-Type": "application/json"},
            verify=False,
            timeout=10
        )
        
        print(f"URL: {WEBHOOK_URL}")
        print(f"Status Code: {response.status_code}")
        
        if response.status_code == 200:
            print("✅ Successfully sent data")
            print(f"Response: {json.dumps(response.json(), indent=2)}")
            return True
        else:
            print(f"❌ Failed with status code: {response.status_code}")
            print(f"Response: {response.text}")
            return False
            
    except Exception as e:
        print(f"❌ Error: {str(e)}")
        return False

def test_get_latest():
    """Test the /api/latest endpoint to verify data was stored"""
    print_separator("Testing Latest Data Endpoint")
    
    try:
        response = requests.get(f"{BASE_URL}/api/latest", verify=False, timeout=10)
        print(f"URL: {BASE_URL}/api/latest")
        print(f"Status Code: {response.status_code}")
        
        if response.status_code == 200:
            print("✅ Successfully retrieved latest data")
            print(f"Latest POST: {json.dumps(response.json(), indent=2)}")
            return True
        elif response.status_code == 404:
            print("⚠️  No data found (404)")
            return True
        else:
            print(f"❌ Unexpected status code: {response.status_code}")
            return False
            
    except Exception as e:
        print(f"❌ Error: {str(e)}")
        return False

def test_get_all_data():
    """Test the /api/data endpoint to view all stored data"""
    print_separator("Testing All Data Endpoint")
    
    try:
        response = requests.get(f"{BASE_URL}/api/data", verify=False, timeout=10)
        print(f"URL: {BASE_URL}/api/data")
        print(f"Status Code: {response.status_code}")
        
        if response.status_code == 200:
            data = response.json()
            print(f"✅ Successfully retrieved all data")
            print(f"Total requests stored: {data.get('total_requests', 0)}")
            return True
        else:
            print(f"❌ Failed with status code: {response.status_code}")
            return False
            
    except Exception as e:
        print(f"❌ Error: {str(e)}")
        return False

def test_endpoint():
    """Test the /api/test endpoint"""
    print_separator("Testing Test Endpoint")
    
    try:
        response = requests.get(f"{BASE_URL}/api/test", verify=False, timeout=10)
        print(f"URL: {BASE_URL}/api/test")
        print(f"Status Code: {response.status_code}")
        
        if response.status_code == 200:
            print("✅ Test endpoint is working")
            print(f"Response: {json.dumps(response.json(), indent=2)}")
            return True
        else:
            print(f"❌ Failed with status code: {response.status_code}")
            return False
            
    except Exception as e:
        print(f"❌ Error: {str(e)}")
        return False

def run_all_tests():
    """Run all tests and provide summary"""
    print("\n" + "🚀 "*20)
    print("VERCEL WEBHOOK SERVER TEST SUITE")
    print("🚀 "*20)
    print(f"\nServer URL: {BASE_URL}")
    print(f"Testing started at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    
    results = {
        "Root Endpoint": test_root_endpoint(),
        "Test Endpoint": test_endpoint(),
        "Webhook (No Auth)": test_webhook_without_auth(),
        "Webhook (With Auth)": test_webhook_with_auth(),
        "Latest Data": test_get_latest(),
        "All Data": test_get_all_data()
    }
    
    # Summary
    print_separator("TEST SUMMARY")
    passed = sum(1 for result in results.values() if result)
    total = len(results)
    
    for test_name, result in results.items():
        status = "✅ PASS" if result else "❌ FAIL"
        print(f"{test_name:.<40} {status}")
    
    print(f"\nTotal: {passed}/{total} tests passed")
    
    if passed == total:
        print("\n🎉 All tests passed! Server is working correctly!")
    else:
        print(f"\n⚠️  {total - passed} test(s) failed. Please check the errors above.")
    
    print("\n" + "="*60 + "\n")

if __name__ == "__main__":
    run_all_tests()
