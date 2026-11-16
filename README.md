# Find It Quickly

A CS50 web project for finding nearby venues by category. Python/Flask renders the catalog; browser geolocation and Google Maps/Places display results within a 1 km search radius.

## Run locally

```sh
python -m venv .venv
# Activate .venv for your operating system.
python -m pip install -r requirements.txt
# Set GOOGLE_MAPS_API_KEY in your environment to your own configured browser API key.
python app.py
```

Open http://127.0.0.1:5000. Without a key, the catalog works and map pages explain the missing configuration. Restrict browser API keys by website and API in your provider console; they are visible to visitors by design. API usage may incur provider charges. The original Heroku deployment is historical, not a verified live demo.

## What to review

- `app.py`: catalog loading relative to the source file, category validation, routing and template rendering.
- `static/js/mapa.js`: asynchronous geolocation, nearby search and markers.
- `templates/`: shared layout and data-driven category navigation.

```sh
python -m unittest -v
```

Tests cover catalog rendering, missing-key behavior, invalid categories and routing. Live Maps/Places behavior requires a valid key and browser location permission; these tests do not call Google.

## Scope

Educational prototype, not a production location service. The Maps client uses a legacy Places interface; provider compatibility and geolocation-denial handling need review before deployment. No availability or search-accuracy benchmark is claimed.

[Original video demonstration](https://youtu.be/etIsGT6Zo9U) · [Portfolio](https://gonza055.github.io/)
