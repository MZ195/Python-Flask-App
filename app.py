from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    return '<h1>Hello {}!</h1>'.format("nono")


@app.route('/json')
def json():
    return jsonify({
        'key': 'value',
        'key2': [1, 2, 3, 4, 5]
    })


if __name__ == "__main__":
    app.run(debug=True)
