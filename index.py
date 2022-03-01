from flask import Flask

app = Flask(__name__)

@app.route('/')
def principal():
    return "Bienvenido a Lollafalopa. Mucha droga en camino."

if __name__ == '__main__':
    app.run()

