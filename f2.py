from flask import Flask

# variable rules: a part ot URL is used as parameter of function
app=Flask(__name__) # take name of current module as argument
app.debug=True
# app.route(rule, options) rule parameter represent URL of "app"
@app.route('/hello/<name>')
# main "Hello World " program
def hello_world(name):
    return "Hello World!"+name

# app.run(host, port, debug, options)
# host: Defaults to 127.0.0.1 (localhost). ‘0.0.0.0’ have server available externally
if __name__=="__main__":
    app.run(host="127.0.0.1", debug=True)
    
