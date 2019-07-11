from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def index():
	return 'hello world'

@app.route('/predict/<name>')
def predict(name):
	data = {'name':name}
	return jsonify(data),200


if __name__ == '__main__':
	app.run()
