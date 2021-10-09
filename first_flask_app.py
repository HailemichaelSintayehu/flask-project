from types import resolve_bases
from flask import Flask,render_template,url_for,redirect,request,session
from datetime import timedelta


app = Flask(__name__)
app.secret_key ="helloww"
app.permanent_session_lifetime=timedelta(days=5)
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/login",methods=["POST","GET"])
def login():
    if request.method == "POST":
      session.permanent = True
      res=request.form["nm"]
      session["many"]=res
      return redirect(url_for("user"))   
    else:
        return render_template("login.html")

@app.route("/user")
def user():
    if "many" in session:
        res=session["many"]
        return f"<h1> {res}  </h1>"
    else:
        if "many" in session:
            return redirect(url_for("user"))
        return redirect(url_for("login"))
@app.route("/logout")
def logout():
    session.pop("many",None)
    return redirect(url_for("login"))
if __name__=='__main__':
    app.run(debug=True)
