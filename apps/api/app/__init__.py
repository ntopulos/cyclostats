from flask import Flask

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
  return "Hi Pedros, I am the API."

@app.route('/mapage')
def mapage():
  return "Ma page test"
