import datetime
import os

from flask import Flask, Response, render_template, url_for, redirect, abort
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import text

app = Flask(__name__, static_folder='assets')
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
app.config['SQLALCHEMY_ECHO'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Body(db.Model):
    __tablename__ = 'bodies'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.Text)
    state = db.Column(db.String(2))
    website = db.Column(db.Text)
    slug = db.Column(db.String(255))
    #legislative_terms = db.relationship('LegislativeTerm', backref='Body', lazy=True)

class LegislativeTerm(db.Model):
    __tablename__ = 'legislative_terms'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    body_id = db.Column(db.Integer, db.ForeignKey('bodies.id'))
    term = db.Column(db.Integer)
    starts_at = db.Column(db.Date)
    ends_at = db.Column(db.Date)

class Paper(db.Model):
    __tablename__ = 'papers'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    body_id = db.Column(db.Integer, db.ForeignKey('bodies.id'))
    legislative_term = db.Column(db.Integer)
    reference = db.Column(db.Text)
    title = db.Column(db.Text)
    contents = db.Column(db.Text)
    page_count = db.Column(db.Integer)
    url = db.Column(db.Text)
    published_at = db.Column(db.Date)
    slug = db.Column(db.String(255))
    contains_table = db.Column(db.Boolean)
    doctype = db.Column(db.Text)
    frozen_at = db.Column(db.Boolean)
    source_url = db.Column(db.Text)
    contains_classified_information = db.Column(db.Boolean)

    DOCTYPE_MINOR_INTERPELLATION = 'minor'
    DOCTYPE_MAJOR_INTERPELLATION = 'major'
    DOCTYPE_WRITTEN_INTERPELLATION = 'written'

    def full_reference(self):
        return '%d/%s' % (self.legislative_term, self.reference)

    def doctype_human(self):
        return {
            self.DOCTYPE_MINOR_INTERPELLATION: 'kleine Anfrage',
            self.DOCTYPE_MAJOR_INTERPELLATION: 'große Anfrage',
            self.DOCTYPE_WRITTEN_INTERPELLATION: 'schriftliche Anfrage'
        }.get(self.doctype, '')

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

@app.route('/info/')
def info():
    return render_template('info/index.html')

@app.route('/search')
def search():
    return abort(501)

@app.route('/<body>/<int:legislative_term>/<slug>/viewer')
def paper_viewer(body, legislative_term, slug):
    return 'FIXME'

@app.route('/<body>/<int:legislative_term>/<slug>.pdf')
def paper_pdf(body, legislative_term, slug):
    return 'FIXME'

@app.route('/<body>/<int:legislative_term>/<slug>.json')
def paper_json(body, legislative_term, slug):
    return 'FIXME'

@app.route('/<body>/<int:legislative_term>/<slug>.txt')
def paper_txt(body, legislative_term, slug):
    return 'FIXME'

@app.route('/<body>/<int:legislative_term>/<slug>')
def paper(body, legislative_term, slug):
    body = Body.query.filter_by(slug=body).first_or_404()
    paper = Paper.query.filter_by(body_id=body.id, legislative_term=legislative_term, slug=slug).first_or_404()
    return render_template('paper/show.html', body=body, paper=paper)

@app.route('/<body>/<int:legislative_term>')
def legislative_term(body, legislative_term):
    return 'FIXME'

@app.route('/<body>')
def body(body):
    return 'FIXME'

@app.route('/recent.atom')
def recent_atom():
    return 'FIXME'

@app.route('/recent')
def recent():
    return 'FIXME'

@app.route('/')
def index():
    bodies = Body.query.order_by(text("state != 'BT', name ASC")).all()
    count= Paper.query.count()
    return render_template('index.html', bodies=bodies, count=count)

if __name__ == '__main__':
    app.run()
