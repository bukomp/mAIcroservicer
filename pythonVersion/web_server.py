from flask import Flask, request, jsonify
import os
import subprocess

app = Flask(__name__)


@app.route('/')
def home():
  return 'Hello, World!'


@app.route('/api/test')
def test():
  try:
    result = subprocess.run(
        ['echo', 'Connection Test'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if result.stderr:
      return jsonify(error=result.stderr.decode().strip()), 500
    return jsonify(message=result.stdout.decode().strip())
  except Exception as e:
    return jsonify(error=str(e)), 500


@app.route('/api/range')
def range():
  min = request.args.get('min', type=int)
  max = request.args.get('max', type=int)
  number = request.args.get('number', type=int)

  if min is None or max is None or number is None:
    return jsonify(error='Please provide min, max and number parameters'), 400

  if number < min or number > max:
    return jsonify(error='Number is out of the provided range'), 400

  try:
    result = subprocess.run(['cli_app', str(min), str(max), str(
        number)], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if result.stderr:
      return jsonify(error=result.stderr.decode().strip()), 500
    return result.stdout.decode().strip()
  except Exception as e:
    return jsonify(error=str(e)), 500


if __name__ == '__main__':
  port = int(os.getenv('PORT', 3000))
  host = str(os.getenv('HOST', '0.0.0.0'))
  app.run(port=port, host=host)
