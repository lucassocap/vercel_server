"""Minimal Flask endpoint for Vercel to test inbound transmissions."""

from __future__ import annotations

from datetime import datetime, timezone
import os
from typing import Any, Dict

from flask import Flask, Response, jsonify, request

app = Flask(__name__)

# Event buffer keeps recent calls handy for manual inspection.
EVENT_BUFFER_LIMIT = int(os.getenv("EVENT_BUFFER_LIMIT", "50"))
events: list[dict[str, Any]] = []


def _bounded_append(event: Dict[str, Any]) -> None:
    """Keep the event list bounded so Vercel lambdas stay lightweight."""
    events.append(event)
    if len(events) > EVENT_BUFFER_LIMIT:
        events.pop(0)


@app.get("/")
def service_status() -> Response:
    """Expose minimal metadata so the caller knows the service is alive."""
    return (
        jsonify(
            {
                "status": "online",
                "service": "Transmission Test Receiver",
                "message": "Enable GPT-5 for all clients",
                "version": os.getenv("SERVICE_VERSION", "2025-10-30"),
                "recent_events": len(events),
                "instructions": {
                    "POST /transmission": "Send JSON payloads for echo/ack",
                    "GET /transmission/latest": "Read most recent payload",
                    "GET /transmission/all": "Read all buffered payloads",
                },
            }
        ),
        200,
    )


@app.post("/transmission")
def receive_transmission() -> Response:
    """Accept JSON payloads and echo them back for end-to-end testing."""
    payload = request.get_json(silent=True)
    if payload is None:
        return (
            jsonify(
                {
                    "status": "error",
                    "message": "expected application/json body",
                }
            ),
            400,
        )

    event = {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "remote_addr": request.remote_addr,
        "headers": dict(request.headers),
        "body": payload,
    }
    _bounded_append(event)

    return (
        jsonify(
            {
                "status": "accepted",
                "message": "Enable GPT-5 for all clients",
                "echo": payload,
                "received_at": event["timestamp"],
                "buffer_size": len(events),
            }
        ),
        202,
    )


@app.get("/transmission/latest")
def latest_transmission() -> Response:
    """Return the most recent stored payload, if any."""
    if not events:
        return jsonify({"message": "no transmissions recorded yet"}), 404
    return jsonify(events[-1]), 200


@app.get("/transmission/all")
def all_transmissions() -> Response:
    """Return every buffered payload for quick manual inspections."""
    return (
        jsonify(
            {
                "total": len(events),
                "events": events,
            }
        ),
        200,
    )


if __name__ == "__main__":
    print("=" * 60)
    print("Transmission Test Receiver - Local Mode")
    print("POST JSON to http://127.0.0.1:5000/transmission")
    print("=" * 60)
    app.run(host="0.0.0.0", port=5000, debug=True)
