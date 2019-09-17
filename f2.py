import flask as fl
# variable rules: a part ot URL is used as parameter of function
app=fl.Flask(__name__) # take name of current module as argument
app.debug=True
# app.route(rule, options)  arguments in URL of "app" in <> can be used as argument
# int specify data type. if input does not match data type, it will 404
@app.route('/hello/<name>/<int:id>')
# "Hello World " program
def hello_world(name, id):
    return "Hello World!"+name+" your id is: "+str(id)

# can have many URLs for one flask object
@app.route('/pow/<value>/<pow>')
def power(value, pow):
    result=1
    valuenum=float(value)
    pownum=int(pow)
    for index in range(pownum):
        result*=valuenum
    return str(result)

# redirect: redirect the url to the specified one
# url_for: return an url bound to specified function, name and id are passed to the formal parameter of that function
@app.route('/select/<arg>/<val1>/<val2>')
def choose(arg, val1, val2):
    if arg=='power':
        return fl.redirect(fl.url_for('power', value=float(val1), pow=int(val2)))
    elif arg=='hello_world':
        return fl.redirect(fl.url_for('hello_world', name=val1, id=int(val2)))
if __name__=="__main__":
    app.run(host='0.0.0.0')
    
