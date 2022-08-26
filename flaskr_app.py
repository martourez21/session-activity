from flask import Flask

app = Flask(__name__)

@app.route('/tests')
def tests():
    return True
