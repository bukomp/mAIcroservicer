from flask import Flask, jsonify, request
import cli


app = Flask(__name__)


@app.route("/")
def home():
    return "Welcome to the CLI and Web Server project!"


@app.route("/test")
def test():
    return "This is a test route."


@app.route("/range")
def generate_random_numbers_route():
    minimum = int(request.args.get('minimum', 0))
    maximum = int(request.args.get('maximum', 100))
    count = int(request.args.get('count', 10))

    numbers = cli.generate_random_numbers(minimum, maximum, count)
    return jsonify(numbers)


if __name__ == '__main__':
    app.run(host='0.0.0.0')