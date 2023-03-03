from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello, World! Ceci est le résultat du TP'

if __name__ == '__main__':
    app.run(port=5000, host="0.0.0.0")
