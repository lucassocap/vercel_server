# Vercel Webhook Server Tests

Test suite for the deployed Vercel webhook server.

## Running Tests

### Prerequisites

Install required package:
```bash
pip install requests
```

### Run All Tests

```bash
cd test
python test_vercel_webhook.py
```

## What Gets Tested

1. **Root Endpoint** (`GET /`)
   - Verifies server is online
   - Checks service information

2. **Test Endpoint** (`GET /api/test`)
   - Verifies test endpoint is working
   - Returns server status

3. **Webhook Without Auth** (`POST /api/webhook`)
   - Tests that unauthorized requests are rejected
   - Should return 401 Unauthorized

4. **Webhook With Auth** (`POST /api/webhook`)
   - Tests authenticated POST requests
   - Should return 200 OK
   - Verifies data is accepted

5. **Latest Data** (`GET /api/latest`)
   - Retrieves the most recent POST received
   - Verifies data storage is working

6. **All Data** (`GET /api/data`)
   - Retrieves all stored requests
   - Shows total count of requests

## Expected Results

All tests should pass (✅):
- Root endpoint returns 200
- Test endpoint returns 200
- Webhook without auth returns 401 (correct rejection)
- Webhook with auth returns 200 (data accepted)
- Latest data endpoint returns 200
- All data endpoint returns 200

## Server URL

Current deployment: `https://vercel-server-lyart-theta.vercel.app`

## Authentication

- Username: `dayforce`
- Password: `envalior2025`

(Set as environment variables in Vercel dashboard)
