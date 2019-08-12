kleineanfragen-static
=====================

This project provides a static site generator for [kleineAnfragen.de](https://kleineanfragen.de) based on flask that tries to replicate all urls, except search, email notifications, api and reporting.

Usage
-----
Download a database dump from https://kleineanfragen.de/info/daten and import it into a locally running postgres.

Install stuff with `pip install -r requirements.txt`

Run development server with `DATABASE_URL='postgres://user@localhost/kleineanfragen' FLASK_DEBUG=1 python app.py`

Create static pages with `python freeze.py`
