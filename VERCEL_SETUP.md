# ✅ Vercel Deployment — October 31, 2025

## Status: PUSHED TO GITHUB ✅

✅ Committed changes to GitHub  
✅ `main.py` with Basic Auth restored  
✅ `vercel.json` configuration fixed  
✅ Ready for Vercel to auto-deploy

---

## NOW DO THIS IN YOUR BROWSER 👇

### 1. Go to Vercel Dashboard

Open: https://vercel.com/dashboard

### 2. Find Your Webhook Project

Look for: **"vercel_server"** or your project name

### 3. Set Environment Variables

1. Click **Settings** (top menu of your project)
2. Go to **Environment Variables** (left sidebar)
3. Add **two new variables:**

   **Variable 1:**
   - Name: `WEBHOOK_USERNAME`
   - Value: `dayforce`
   - Environments: Select **Production** checkbox
   - Click **Add**

   **Variable 2:**
   - Name: `WEBHOOK_PASSWORD`
   - Value: `envalior2025`
   - Environments: Select **Production** checkbox
   - Click **Add**

### 4. Trigger a Redeploy

1. Go to **Deployments** tab (at the top)
2. Look for the latest deployment (should say "Pushed from GitHub")
3. Click the **three dots (⋯)** menu
4. Click **Redeploy**

Or go to **Settings** → **Git** and click "Deploy" button next to your branch.

---

## ✅ You're Done!

Once redeployed, your webhook is live at:

```
https://your-project.vercel.app
```

Test it with:

```powershell
cd "c:\Users\P1285FC\OneDrive - Dayforce HCM Inc\Documents\Projects\envalior_bra\tools"
python test_webhook.py
# Enter: https://your-project.vercel.app/webhook
```

---

## 🔗 Dayforce Configuration

Use these settings in Dayforce:

- **Webhook URL**: `https://your-project.vercel.app/webhook`
- **Auth Type**: Basic Authentication
- **Username**: `dayforce`
- **Password**: `envalior2025`
- **Headers**: `Content-Type: application/json`

---

## Troubleshooting

- **Can't find project?** Check the URL: vercel.com/dashboard
- **Env vars not working?** Make sure you selected "Production" checkbox
- **Still getting 401?** Redeploy after saving env vars
- **Need logs?** Go to Deployments → click deployment → Logs tab

Questions? Check DEPLOY_STEPS.md for more details.
