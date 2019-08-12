kleineanfragen-static
=====================

This project provides a static site generator for [kleineAnfragen.de](https://kleineanfragen.de) based on flask that tries to replicate all urls, except search, email notifications, api and reporting.

Usage
-----
Download a database dump from https://kleineanfragen.de/info/daten and import it into a locally running postgres.

Install stuff with `pip install -r requirements.txt`

Run development server with `DATABASE_URL='postgres://user@localhost/kleineanfragen' FLASK_DEBUG=1 python app.py`

Create static pages with `python freeze.py`


Background
----------

This project exists, because [kleineAnfragen.de is going to sleep soon](https://kleineanfragen.de/info/stilllegung). Because I want to be a nice internet citizen, I'll try to respect [Cool URIs don't change](https://www.w3.org/Provider/Style/URI) and want to make preperations to put all the stuff into the [Internet Archive](https://archive.org).

The first draft of this code uses database access with the available [database dumps](https://kleineanfragen.de/info/daten). For a later iteration it would be interesting to try if this could be replaced by consuming the [OParl](https://oparl.org) [API of kleineAnfragen](https://api.kleineanfragen.de/oparl/v1). This would make the project reusable and maybe even interesting for civic tech people and municipalities that want to replace the UI of their OParl compatible system.

Things that cannot be done with a static site generator, like search and the email notification and report forms are out of scope for this project. Returning `501 Not Implemented` is fine for these urls.
