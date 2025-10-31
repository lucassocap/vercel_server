# 🚀 Vercel Webhook - Quick Setup Card

## ✅ Backend is Ready (GitHub Pushed)
- ✅ `main.py` with Basic Auth
- ✅ `vercel.json` configuration
- ✅ Commit: `f00f9b4` pushed to GitHub

---

## 👉 YOUR ACTION ITEMS (Do This Now)

### 1. Open Browser
```
https://vercel.com/dashboard
```

### 2. Find Your Project
Look for: **vercel_server** (or your webhook project)

### 3. Add Environment Variables
**Go to:** Settings → Environment Variables

**Add Variable 1:**
```
Name:  WEBHOOK_USERNAME
Value: dayforce
Env:   Production ✓
```

**Add Variable 2:**
```
Name:  WEBHOOK_PASSWORD
Value: envalior2025
Env:   Production ✓
```

### 4. Redeploy
**Go to:** Deployments tab
- Find the latest deployment (from GitHub)
- Click three dots (⋯)
- Select **Redeploy**

---

## ✅ Done!
Your webhook is now live at:
```
https://<your-project>.vercel.app/webhook
```

### Test Locally
```powershell
cd tools
python test_webhook.py
# Enter: https://<your-project>.vercel.app/webhook
```

---

## 🎯 Use in Dayforce

**Webhook URL:** `https://<your-project>.vercel.app/webhook`
**Auth Type:** Basic Authentication
**Username:** `dayforce`
**Password:** `envalior2025`

---

### 📝 Notes
- Environment variables take effect immediately after redeploy
- If 401 errors, make sure Production checkbox is selected
- Check Vercel Deployments logs if issues persist
