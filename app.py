from markupsafe import escape
from flask import Response
from flask import Flask
import random
import getdata

app = Flask(__name__)

@app.route('/')
def start():
    f = open("./web/test.html")
    e = f.read()
    f.close()
    return e
@app.route('/recipe/<item>')
def getrec(item):
    try:
        return getdata.recipes[item]
    except:
        return "invalid item"
@app.route('/lang/<item>')
def getname(item):
    final = None
    try:
        final = getdata.lang["item.minecraft." + item]
    except:
        try:
            final = getdata.lang["block.minecraft." + item]
        except:
            final = "invalid item"
    return final
@app.route('/splash')
def splash():
    f = open("./splash.txt")
    r = f.read()
    f.close()
    return random.choice(r.split("\n"))
