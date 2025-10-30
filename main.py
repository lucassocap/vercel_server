"""Minimal Flask webhook receiver for Vercel deployments."""

from datetime import datetime
from flask import Flask, jsonify, request

app = Flask(__name__)

# In-memory payload list (each serverless instance holds its own copy)
payloads: list[dict] = []


@app.route("/", methods=["GET"])
def status() -> tuple[dict, int]:
    """Expose basic service metadata for quick smoke-tests."""
    return (
        jsonify(
            {
                "status": "online",
                "service": "Vercel Flask Webhook",
                "count": len(payloads),
                "endpoints": {
                    "POST /webhook": "Send any test payload",
                    "GET /latest": "Retrieve most recent payload",
                    "GET /data": "Retrieve all stored payloads",
                },
            }
        ),
        200,
    )


@app.route("/webhook", methods=["POST"])
def webhook() -> tuple[dict, int]:
    """Accept and store incoming webhook payloads for inspection."""
    body = request.get_json(silent=True)
    if body is None:
        body = request.form.to_dict() or request.data.decode("utf-8")

    entry = {
        "timestamp": datetime.utcnow().isoformat(),
        "headers": dict(request.headers),
        "method": request.method,
        "remote_addr": request.remote_addr,
        "body": body,
    }
    payloads.append(entry)

    # Keep the list bounded to avoid oversized Lambda bundles.
    if len(payloads) > 100:
        payloads.pop(0)

    return jsonify({"message": "received", "stored": len(payloads)}), 200


@app.route("/latest", methods=["GET"])
def latest() -> tuple[dict, int]:
    """Return the most recent webhook payload, if any."""
    if not payloads:
        return jsonify({"message": "no payloads yet"}), 404
    return jsonify(payloads[-1]), 200


@app.route("/data", methods=["GET"])
def data() -> tuple[dict, int]:
    """Return every payload captured during this process lifetime."""
    return jsonify({"count": len(payloads), "items": payloads}), 200


if __name__ == "__main__":
    # Helpful banner when running locally.
    print("=" * 40)
    print("Vercel Flask Webhook - Local Mode")
    print("Send POSTs to http://127.0.0.1:5000/webhook")
    print("=" * 40)
    app.run(host="0.0.0.0", port=5000, debug=True)
