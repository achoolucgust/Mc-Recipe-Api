from flask import Flask
from flask import Response
app = Flask(__name__)

@app.route('/')
def hello_world():
    return Response(status=200)
