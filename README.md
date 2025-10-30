# Dayforce Webhook Receiver - Vercel

Flask serverless function to receive webhook POSTs from Dayforce.

## Quick Deploy to Vercel

1. **Install Vercel CLI:**
```bash
npm install -g vercel
```

2. **Login to Vercel:**
```bash
vercel login
```

3. **Deploy:**
```bash
vercel
```

4. **Set Environment Variables** (in Vercel dashboard):
   - `WEBHOOK_USERNAME` = `dayforce`
   - `WEBHOOK_PASSWORD` = `envalior2025`

## Your Webhook URL

After deployment, your webhook URL will be:
```
https://your-project-name.vercel.app/webhook
```

## Endpoints

- `POST /webhook` - Main webhook endpoint (requires Basic Auth)
- `GET /data` - View all received data
- `GET /latest` - View latest POST
- `GET /test` - Test endpoint
- `GET /` - Service status

## Authentication

Basic Authentication with credentials from environment variables.

## Dayforce Configuration

Use in Dayforce:
- **API URL**: `https://your-project-name.vercel.app/webhook`
- **Authentication Type**: Basic Authentication
- **Username**: `dayforce`
- **Password**: `envalior2025`
- **Headers**: `Content-Type: application/json`
