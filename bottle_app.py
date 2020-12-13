# A very simple Bottle Hello World app for you to get started with...
from bottle import default_app, route, post, get, template, run, static_file

@route('/')
def gettingerMain():
    return template("./views/gettingerMain.html")

@route('/beefBill')
def beefBill():
    return template("./views/beefBill.html")

@post('/beefRecipt')
def beefRecipt():
    return template("./views/beefRecipt.html")

@route('/hogBill')
def hogBill():
    return template("./views/hogBill.html")

@post('/hogRecipt')
def hogRecipt():
    return template("./views/hogRecipt.html")

@route('/lambBill')
def lambBill():
    return template(",/views/lambBill.html")
	
@post('/lambRecipt')
def lambRecipt():
    return template("./views/lambRecipt.html")

@route('/setPrices')
def setPrices():
    return template("./views/setPrices.html")

@post('/priceChange')
def priceChange():
    return template("./views/priceChange.html")

@route('/css/<filename>')
def css(filename):
    return static_file(filename, root='./views/css')
application=default_app()

run(host="localhost", port=8080, debug=True)
