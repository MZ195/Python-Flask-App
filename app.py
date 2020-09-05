from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    return '<h1>Hello {}!</h1>'.format("nono")


@app.route('/home', methods=['POST', 'GET'], defaults={'name': 'Mr.X'})
@app.route('/home/<int:name>', methods=['POST', 'GET'])
def home(name):
    return '<h1>Hello {}, You are on the home page!</h1>'.format(name)


@app.route('/query')
def query():
    name = request.args.get('name')
    location = request.args.get('location')
    return '<h1>Hi {}. You are from {}. You are on the query page!</h1>'.format(name, location)


@app.route('/theform')
def theForm():
    return '''<form method="POST" action="/process">
    <input type="text" name="name">
    <input type="text" name="location">
    <input type="submit">
    </form>
    '''


@app.route('/process', methods=['POST'])
def process():
    name = request.form['name']
    location = request.form['location']
    return '<h1>Hi {}. You are from {}. You have submitted the form successfully!</h1>'.format(name, location)


@app.route('/processJson', methods=['POST'])
def processJson():
    data = request.get_json()

    name = data["name"]
    location = data["location"]
    randomList = data["list"]

    return jsonify({'result': 'Success!'})


@app.route('/json')
def json():
    return jsonify({
        'key': 'value',
        'key2': [1, 2, 3, 4, 5]
    })


if __name__ == "__main__":
    app.run(debug=True)
