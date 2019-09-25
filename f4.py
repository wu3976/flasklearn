import flask as f
app = f.Flask(__name__)
# Flask can return a String of html to the method binding to that URL.
@app.route('/')
def index():
    # f.render_template return the String of html in the specified file. This method would try to find file in the template.
   return f.render_template("page.html")

# variable data can be inserted dynamically through jinja 2 rendering engine
@app.route('/dynamic/<user>')
def dynamic(user):
    return f.render_template("test.html", input=user) # input argument is {{input}} in test.html, {{...}} represent value

@app.route('/dynamic2/<score>')
def dynamic2(score):
    score=float(score)
    return f.render_template("test2.html", score=score) # {%...%} represent statements
# {# ... #} for Comments not included in the template output
# # ... ## for Line Statements
@app.route('/onclick', methods=['POST', 'GET'])
def onclick ():
    return f.render_template("Onclick.html")

if __name__ == '__main__':
   app.run(debug = True, host='0.0.0.0', port='5000')