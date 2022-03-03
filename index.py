from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def principal():
    return render_template('index.html')

@app.route('/grilla')
def Grilla():
    return render_template('grilla.html')

@app.route('/horariosdia1')
def horariosdia1():
    return render_template('horariosdia1.html')

@app.route('/horariosdia2')
def horariosdia2():
    return render_template('horariosdia2.html')

@app.route('/showkids')
def showkids():
    return render_template('showkids.html')

if __name__ == '__main__':
    app.run(debug=True, port=2022)