from flask import render_template

from homehub import app


@app.route('/')
def index():
    return render_template("floorplan.html")


@app.route('/why')
def why():
    return render_template("why.html")
