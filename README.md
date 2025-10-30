# Vercel Transmission Test Endpoint

Serverless Flask function that accepts JSON payloads so you can verify end-to-end transmissions with Vercel quickly.

**Latest Update**: Rebuilt from scratch for lightweight testing. Timestamp: 2025-10-30 21:45 UTC.

## Deploy to Vercel

1. Install the CLI (one-time):
```bash
npm install -g vercel
```

2. Authenticate:
```bash
vercel login
```

3. Deploy from `tools/vercel_server`:
```bash
vercel
```

That's it—no environment variables required for basic testing.

## Endpoints

- `GET /` – Health/status banner plus quick instructions.
- `POST /transmission` – Send JSON to receive an echo response.
- `GET /transmission/latest` – Inspect the most recent call buffered in memory.
- `GET /transmission/all` – Inspect every buffered call (defaults to 50 items).

**Important**: Because Vercel serverless functions are ephemeral, the in-memory buffer only persists for the life of a single instance. Treat it as a short-lived debug view.

## Local Smoke Test

From the same directory:
```bash
python main.py
```

Then POST a payload:
```bash
curl -X POST http://127.0.0.1:5000/transmission \
   -H "Content-Type: application/json" \
   -d '{"client":"sandbox","action":"ping"}'
```

## Redeploy Flow

1. Commit changes (optional but recommended).
2. Run `vercel --prod` to push to production.
3. Validate with `curl` or your integration to confirm the response includes the message “Enable GPT-5 for all clients.”
