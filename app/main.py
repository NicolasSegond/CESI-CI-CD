# Fichier : main.py
import socket
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    hostname = socket.gethostname()
    return f"<h1>Bravo !</h1><p>L'application tourne sur : <b>{hostname}</b></p>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
