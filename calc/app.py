from flask import Flask, request
from operations import add, sub, mult, div
app = Flask(__name__)

# Put your app in here.

# Make a Flask app that responds to 4 different routes.
# Each route does a math operation with two numbers, a and b,
#  which will be passed in as URL GET-style query parameters.

# /add
# Adds a and b and returns result as the body.


@app.route('/add')
def adds():
    """Adds a and b and returns result as the body."""
    a = int(request.args["a"])
    b = int(request.args["b"])

    return f"{add(a,b)}"

# /sub
# Same, subtracting b from a.


@app.route('/sub')
def subtracts():
    """Subtracts b from a and returns result as the body."""
    a = int(request.args["a"])
    b = int(request.args["b"])

    return f"{sub(b, a)}"

# /mult
# Same, multiplying a and b.


@app.route('/mult')
def multiplys():
    """Multiplys b and a and returns result as the body."""
    a = int(request.args["a"])
    b = int(request.args["b"])

    return f"{mult(b, a)}"

# /div
# Same, dividing a by b.


@app.route('/div')
def divides():
    """Divides b from a and returns result as the body."""
    a = int(request.args["a"])
    b = int(request.args["b"])

    return f"{div(a,b)}"
# For example, a URL like http://localhost:5000/add?a=10&b=20 should return a string response of exactly 30.


@app.route('/math/<operation>')
def do_math(operation):

    OPERATIONS = {
        "add": add,
        "sub": sub,
        "mult": mult,
        "div": div
    }
    a = int(request.args["a"])
    b = int(request.args["b"])

    return f"{OPERATIONS[operation](a, b)}"
