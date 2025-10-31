# Dayforce Webhook Receiver — Vercel

Secure Flask serverless function to receive POSTs from Dayforce and inspect payloads during migrations.

**Configuration**: `vercel.json` pins the Python builder and routes every request to `main.py`.

**Latest Update**: Basic Auth restored (2025-10-31 09:00). Local scripts and Vercel deployments now behave identically.

## Quick Deploy to Vercel

1. **Install Vercel CLI**
	```bash
	npm install -g vercel
	```

2. **Login to Vercel**
	```bash
	vercel login
	```

3. **Initial Deploy (run inside `tools/vercel_server`)**
	```bash
	vercel
	```

4. **Set Environment Variables** (Dashboard → Settings → Environment Variables)
	- `WEBHOOK_USERNAME` = `dayforce`
	- `WEBHOOK_PASSWORD` = `envalior2025`
	- *(Optional)* `PYTHON_VERSION` = `3.11`

5. **Redeploy after saving env vars**
	```bash
	vercel deploy --prod
	```

6. **Inspect Deployment Logs (if something fails)**
	```bash
	vercel logs <deployment-url>
	```

## Endpoints

- `POST /webhook` – Primary webhook endpoint (requires Basic Auth)
- `GET /data` – Lists every payload captured by the current instance
- `GET /latest` – Returns the most recent payload
- `GET /test` – Lightweight health check
- `GET /` – Service metadata

## Local Smoke Test

```bash
cd tools/vercel_server
python main.py
# in another shell
python ..\test_webhook_auto.py
```

The automated test validates both the authenticated and unauthenticated flows.

## Dayforce Configuration

- **API URL**: `https://<your-project-name>.vercel.app/webhook`
- **Authentication Type**: Basic Authentication
- **Username**: `dayforce`
- **Password**: `envalior2025`
- **Headers**: `Content-Type: application/json`
