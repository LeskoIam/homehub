from flask import render_template

from homehub import app


@app.route('/')
def index():
    return render_template("floorplan.html")
