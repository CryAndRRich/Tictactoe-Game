from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/variations', methods = ['POST'])
def variations():
    msg = {'player1': request.form['player1'],
           'player2': request.form['player2']}
    return render_template('variations.html', msg = msg)

@app.route('/basic')
def basic():
    return "hello basic"

@app.route('/hexagonal')
def hexagonal():
    return render_template('hexagonal.html')

@app.route('/qubic')
def qubic():
    return render_template('qubic.html')