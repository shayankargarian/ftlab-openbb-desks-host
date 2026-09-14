import json
import os
from pathlib import Path

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse, PlainTextResponse
import uvicorn

ROOT = Path(__file__).resolve().parent
WIDGETS = json.loads((ROOT / "widgets.json").read_text(encoding="utf-8"))
APPS = json.loads((ROOT / "apps.json").read_text(encoding="utf-8"))
CORS = [
    "https://pro.openbb.co",
    "https://pro.openbb.dev",
    "https://workspace.openbb.co",
    "http://localhost:1420",
]
app = FastAPI(title="FTLAB OpenBB Workspace backend", version="0.1.0")
app.add_middleware(
    CORSMiddleware,
    allow_origins=CORS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {
        "Info": "FTLAB OpenBB Workspace custom backend",
        "profile": os.environ.get("DESK_PROFILE", "shayan"),
        "apps": ["Desk A: General markets", "Desk B: Dubai overlay"],
        "source": "https://github.com/shayankargarian/ftlab-openbb-desks",
    }

@app.get("/health")
def health():
    return {
        "ok": True,
        "profile": os.environ.get("DESK_PROFILE", "shayan"),
        "friend_draft_never_publish": False,
        "openbb": {
            "installed": False,
            "error": "Hosted go-live serves Workspace JSON. OpenBB ODP runs in the local venv.",
            "fred_key_present": False,
            "fmp_key_present": False,
            "profile": "shayan",
        },
        "pulse": "stub_only",
        "live_pulse": False,
        "skip_dld_api_gateway": True,
        "saudi_or_extra_gcc_connectors": False,
        "desk_owns": "openbb_only",
    }

@app.get("/widgets.json")
def widgets():
    return JSONResponse(WIDGETS)

@app.get("/apps.json")
def apps():
    return JSONResponse(APPS)

@app.get("/briefing", response_class=PlainTextResponse)
def briefing():
    return "# FTLAB OpenBB desks\n\nShared custom backend. Desk A is general markets. Desk B is the Dubai Pulse stub overlay. Friend is draft-never-publish and is not hosted here.\n"

@app.get("/provider_status", response_class=PlainTextResponse)
def provider_status():
    return "# OpenBB provider status\n\nThis public host serves /widgets.json and /apps.json. OpenBB ODP is installed locally. Empty tables are not fake stats.\n"

@app.get("/dubai_pulse_notes", response_class=PlainTextResponse)
def dubai_pulse_notes():
    return "# Dubai Pulse open DLD (stub)\n\nLive Pulse is not wired. No invented figures. DLD API Gateway skipped.\n"

@app.get("/gcc_overlay_notes", response_class=PlainTextResponse)
def gcc_overlay_notes():
    return "# Desk B overlay notes\n\nDubai Pulse stubs on the same backend as Desk A. No Saudi or extra GCC connectors.\n"

@app.get("/entity_risk_stubs", response_class=PlainTextResponse)
def entity_risk_stubs():
    return "# Entity / risk connectors (not wired)\n\nNo screening results. Empty by design.\n"

@app.get("/custom_connectors", response_class=PlainTextResponse)
def custom_connectors():
    return "# Custom backends (adapt)\n\nOpenSanctions, Guardian, Companies House, Finnhub, UN Comtrade, World Bank, GDELT, Frankfurter, Wikidata, GLEIF: stub.\n"

@app.get("/dubai_pulse")
def dubai_pulse():
    return []

@app.get("/equity_quotes")
@app.get("/equity_history")
@app.get("/fx_history")
@app.get("/macro_fred")
@app.get("/credit_fred")
@app.get("/world_news")
@app.get("/company_news")
@app.get("/sec_filings")
def empty_table():
    return []

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=int(os.environ.get("PORT", "6910")))
