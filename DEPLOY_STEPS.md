# Vercel Deployment Checklist — 2025-10-31

## Status: Ready to Deploy ✅

Local smoke test **PASSED**:
- ✅ POST with Basic Auth → 200 OK, payload stored
- ✅ POST without auth → 401 Unauthorized (correctly rejected)
- ✅ GET /latest → Returns most recent payload
- ✅ GET /data → Lists all stored payloads

---

## Step 1: Set Environment Variables in Vercel Dashboard

1. Go to **Vercel Dashboard** → Find your project
2. Click **Settings** → **Environment Variables**
3. Add two new variables:
   - **Name**: `WEBHOOK_USERNAME` → **Value**: `dayforce`
   - **Name**: `WEBHOOK_PASSWORD` → **Value**: `envalior2025`
4. Click **Save** on each variable

---

## Step 2: Deploy to Production

From PowerShell in `tools/vercel_server`:

```powershell
cd "c:\Users\P1285FC\OneDrive - Dayforce HCM Inc\Documents\Projects\envalior_bra\tools\vercel_server"
vercel deploy --prod
```

Expected output:
```
Production Deployment (vercel deploy --prod)
▲ Vercel CLI 31.0.0
✓ Linked to your-project
✓ Building...
✓ Success! Production URL: https://your-project.vercel.app
```

---

## Step 3: Verify the Deployment

### Option A: Quick HTTP GET
```powershell
Invoke-RestMethod -Uri "https://your-project.vercel.app/" -Method GET
```

Should return service metadata with status "online".

### Option B: Full Automated Test
```powershell
cd "c:\Users\P1285FC\OneDrive - Dayforce HCM Inc\Documents\Projects\envalior_bra\tools"
python test_webhook.py
# When prompted, enter: https://your-project.vercel.app/webhook
```

---

## Troubleshooting

### Deployment fails?
Check Vercel build logs:
```powershell
vercel logs https://your-project.vercel.app
```

### Endpoint returns 500?
- Confirm env vars are set in Vercel dashboard (they may not apply immediately)
- Redeploy: `vercel deploy --prod`

### Authentication failing?
- Double-check credentials: `dayforce` / `envalior2025`
- Verify environment variables are deployed (not just saved)

---

## Dayforce Integration

Once deployed and verified, use this URL in Dayforce:

**Webhook URL**: `https://your-project.vercel.app/webhook`
**Authentication**: Basic Auth
**Username**: `dayforce`
**Password**: `envalior2025`
**Content-Type**: `application/json`

---

## Ready? Let's Go! 🚀

1. Set env vars in Vercel dashboard ← **DO THIS FIRST**
2. Run `vercel deploy --prod`
3. Test with `test_webhook.py`
4. Configure Dayforce

Questions? Check `README.md` or `tools/flask_post_server.py` for the local reference.
