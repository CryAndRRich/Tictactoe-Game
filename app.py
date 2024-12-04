from flask import Flask, render_template, request, session

app = Flask(__name__)
app.secret_key = 'your_secret_key'

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/variations', methods = ['POST'])
def variations():
    msg = {'player1': request.form['player1'],
            'player2': request.form['player2']}

    session['message'] = msg

    return render_template('variations.html', msg = msg)

@app.route('/variations/back', methods=['POST'])
def variations_back():
    return render_template('variations.html', msg = session.get('message'))

@app.route('/basic')
def basic():
    return render_template('variants_template/basic.html', msg = session.get('message'))

@app.route('/hexagonal')
def hexagonal():
    return render_template('variants_template/hexagonal.html', msg = session.get('message'))

@app.route('/qubic')
def qubic():
    return render_template('variants_template/qubic.html', msg = session.get('message'))
