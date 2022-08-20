from flask import render_template

from homehub import app


@app.route('/')
def index():
    print(
        "let me sea wahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahahaha")
    return render_template("floorplan.html")
