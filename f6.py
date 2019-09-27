import flask as f

app=f.Flask(__name__)

@app.route('/')
def index():
    return f.render_template('/f6/index.html')

@app.route('/setCookie', methods=['POST', 'GET'])
def setCookie():
    if f.request.method=='POST':
        address=f.request.form['address_name']
        name=f.request.form['person_name']
        resp=f.make_response(f.render_template('/f6/login.html')) # get response object from return value
        resp.set_cookie('user_info', address) # make a cookie txt file named user_info storing form
        resp.set_cookie('user_name', name)
        return resp

@app.route('/getCookie')
def getCookie():
    user_info=f.request.cookies.get('user_info')
    user_name=f.request.cookies.get('user_name')
    return user_info+"<br>"+user_name

if __name__=="__main__":
    app.run(debug=True)