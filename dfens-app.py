from bottle import route, run
from math import sqrt

@route('/')
def hello():
    resp = "Square root of 2k - %s" % sqrt(2000)
    print(resp)
    return resp

run(host='0.0.0.0', port=80, debug=True)
