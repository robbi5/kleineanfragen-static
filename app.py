from flask import Flask, Response, render_template, url_for, redirect
import datetime

app = Flask(__name__, static_folder='assets')

@app.route('/data')
def data():
    return redirect(url_for('info_daten'))

@app.route('/static/kleineanfragen.svg')
def static_kleineanfragensvg():
    return redirect(url_for('static', filename='kleineanfragen.svg'))

@app.route('/status')
def status():
    text = "STATIC - %s" % datetime.datetime.utcnow().isoformat()
    return Response(text, mimetype='text/plain')

@app.route('/info/daten')
def info_daten():
    return render_template('info/daten.html')

@app.route('/info/kontakt')
def info_kontakt():
    return render_template('info/kontakt.html')

@app.route('/info/datenschutz')
def info_datenschutz():
    return render_template('info/datenschutz.html')

@app.route('/info/mitmachen')
def info_mitmachen():
    return render_template('info/mitmachen.html')

@app.route('/info/spenden')
def info_spenden():
    return render_template('info/spenden.html')

@app.route('/info/stilllegung')
def info_stilllegung():
    return render_template('info/stilllegung.html')

@app.route('/info')
def info():
    return render_template('info/index.html')

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run()
