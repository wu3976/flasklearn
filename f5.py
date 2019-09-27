import flask as f
app=f.Flask(__name__)

@app.route("/")
def student ():
    return f.render_template("/f5/student.html")

@app.route("/result", methods=['POST', 'GET'])
def result():
    if f.request.method == 'POST':
        result=f.request.form.to_dict(flat=False)
        # print(result)
        return f.render_template("/f5/result.html", result=result)

if __name__=="__main__":
    app.run(debug=True)