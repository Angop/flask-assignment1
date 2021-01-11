from flask import Flask
app = Flask(__name__)

@app.route('/') # Tells flask what url triggers our function
def hello_world():
        return 'Hello, World!'

