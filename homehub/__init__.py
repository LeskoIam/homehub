from flask import Flask

app = Flask(__name__)

import homehub.views

if __name__ == '__main__':
    app.run()
