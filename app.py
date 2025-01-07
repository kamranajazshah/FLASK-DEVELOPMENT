from flask import Flask ,redirect,url_for

app= Flask(__name__)
@app.route("/")
def welcome():
    return "Hello world"
@app.route("/success/<int:marks>")
def success(marks):
    return "he has passed the exam"+ str(marks)
@app.route("/fail/<int:marks>")
def fail(marks):
    return "he has failed the exam"+ str(marks)
@app.route("/results/<int:marks>")
def result(marks):
    score=""
    if marks<50:
        score="fail"
    else:
        score="success"
    return redirect(url_for(score,marks=marks))
if __name__=="__main__":
    app.run(debug=True)