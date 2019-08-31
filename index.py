from flask import Flask, render_template, request
import requests, json

# Set up app
app = Flask(__name__)
PORT = 8000

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template("index.html")

@app.route('/tools', methods=['GET', 'POST'])
def tools():
    return render_template("tools.html")

if __name__ == '__main__':
	app.run(
		debug=True,
		host='0.0.0.0',
		port=PORT,
		#ssl_context='adhoc'
	)