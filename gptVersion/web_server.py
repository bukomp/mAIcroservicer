from flask import Flask, jsonify, request
import subprocess
import json

app = Flask(__name__)


@app.route('/')
def home():
  return "Welcome to the home page!"


@app.route('/test')
def test():
  return "Test route is working!"


@app.route('/range')
def range_route():
  min_value = request.args.get('min', default=1, type=int)
  max_value = request.args.get('max', default=100, type=int)
  count = request.args.get('count', default=5, type=int)

  result = subprocess.run(['python', 'cli.py', '--min', str(min_value),
                          '--max', str(max_value), '--count', str(count)], stdout=subprocess.PIPE)
  return jsonify(numbers=json.loads(result.stdout))


if __name__ == "__main__":
  app.run(debug=True)
