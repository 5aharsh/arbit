from flask import Flask, jsonify, render_template
import random, time

app = Flask(__name__)
rng = random.SystemRandom()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/ratio/')
@app.route('/ratio/<int:n>')
def ratio(n=1):
    if n==1:
        result = rng.random()
    else:
        result = [rng.random() for _ in range(n)]
    response = {'result': result, "timestamp": time.time()}   
    return jsonify(response)

@app.route('/dice/')
@app.route('/dice/<int:n>')
def dice(n=1):
    if n==1:
        result=rng.choice([1,2,3,4,5,6])
    else:
        result = [rng.choice([1,2,3,4,5,6]) for _ in range(n)]
    response = {'result': result, "timestamp": time.time()}
    return jsonify(response)

@app.route('/deck/')
@app.route('/deck/<int:n>')
def deck(n=1):
    suite = ['H', 'S', 'C', 'D']
    number = ['A','2','3','4','5','6','7','8','9','10','J','Q','K']
    if n==1:
        result = {'suite': rng.choice(suite), 'number':rng.choice(number)}
    else:
        result = [{'suite': rng.choice(suite), 'number':rng.choice(number)} for _ in range(n)]
    response = {'result': result, "timestamp": time.time()}
    return jsonify(response)

@app.route('/integer/')
@app.route('/integer/<int:max>')
@app.route('/integer/<int:min>/<int:max>')
@app.route('/integer/n/<int:n>')
@app.route('/integer/<int:max>/n/<int:n>')
@app.route('/integer/<int:min>/<int:max>/n/<int:n>')
def integer(min=0, max=99, n=1):
    if n==1:
        result = int(rng.uniform(min, max))
    else:
        result = [int(rng.uniform(min, max)) for _ in range(n)]
    response = {'result': result, "timestamp": time.time()}
    return jsonify(response)

@app.route('/float/')
@app.route('/float/<int:max>')
@app.route('/float/<int:min>/<int:max>')
@app.route('/float/n/<int:n>')
@app.route('/float/<int:max>/n/<int:n>')
@app.route('/float/<int:min>/<int:max>/n/<int:n>')
def float(min=0, max=99, n=1):
    if n==1:
        result = rng.uniform(min, max)
    else:
        result = [rng.uniform(min, max) for _ in range(n)]
    response = {'result': result, "timestamp": time.time()}
    return jsonify(response)

@app.route('/coin/')
@app.route('/coin/<int:n>')
def coin(n=1):
    if n==1:
        result=rng.choice(['H', 'T'])
    else:
        result = [rng.choice(['H','T']) for _ in range(n)]
    response = {'result': result, "timestamp": time.time()}
    return jsonify(response)

@app.route('/set/<string:setstring>/')
@app.route('/set/<string:setstring>/<int:n>')
def set(setstring, n=1):
    setstring = setstring.split(',')
    if n==1:
        result = rng.choice(setstring)
    else:
        result = [rng.choice(setstring) for _ in range(n)]
    response = {'result': result, "timestamp": time.time()}
    return jsonify(response)

if __name__=='__main__':
    app.run()