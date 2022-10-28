from flask import Flask, render_template, url_for, session, redirect
from flask_sslify import SSLify
import os

app = Flask('app')
if 'DYNO' in os.environ: 
    sslify = SSLify(app)


@app.route('/')
def index():
    return render_template("/index.html", page="Home")

@app.route('/mission')
def mission():
    return render_template("/mission.html", page="Mission")

@app.route('/launchhacks')
def launchhacks():
    return render_template("launchhacks.html", page="LaunchHacks I")

@app.route('/about')
def about():
    return render_template("about.html", page="About")

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=1000, debug=True)