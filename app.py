"""Nearby-place search demo. Google Maps runs in the browser."""
import json
import os
from pathlib import Path
from flask import Flask, request, redirect, render_template

app = Flask(__name__)
CATALOG = Path(__file__).parent / 'static' / 'list.json'

@app.route('/')
def mapa():
    with CATALOG.open(encoding='utf-8') as source:
        places = json.load(source)['list']
    place_type = request.args.get('type')
    if not place_type:
        return render_template('inicio.html', lista=places)
    if place_type not in {place['string'] for place in places}:
        return redirect('/')
    return render_template('mapa.html', lista=places, tipo=place_type,
                           maps_api_key=os.environ.get('GOOGLE_MAPS_API_KEY', ''))

@app.errorhandler(404)
def page_not_found(error):
    return redirect('/')

if __name__ == '__main__':
    app.run()
