# Flask is a web application framework written in Python
# test flask installation
from flask import Flask

app=Flask(__name__) # take name of current module as argument
app.debug=True
# app.route(rule, options) rule parameter represent URL of "app"
@app.route('/hello')
# main "Hello World " program
def hello_world():
    return "Hello World!"

# app.run(host, port, debug, options)
# host: Defaults to 127.0.0.1 (localhost). ‘0.0.0.0’ have server available externally
if __name__=="__main__":
    app.run(host="0.0.0.0", debug=True)
    
