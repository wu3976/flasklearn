import flask as fl
from flask import redirect, url_for, request

#request class interact with the web cilent and contains methods to process the user inputs.
app=fl.Flask(__name__)

@app.route("/success/<name>")
def success (name):
    print("Welcome, %s", name)

@app.route("/login", methods=['POST', 'GET']) # specify the method would be used.
# POST: when clients need to upload forms or datas
# GET: when clients only need to get datas
def login ():
    if (request.method=='POST'): # when cilents perform such a method
        user=request.form['nm'] # receive the form submitted by client from 'nm' textfield, assign it to
        # variable user.
        return redirect(url_for('success', name=user))
    else:
        user = request.args.get('nm')
        return redirect(url_for('success', name=user))

if (__name__=='__main__'):
    app.run(debug=True, host='0.0.0.0')
