from types import resolve_bases
from flask import Flask,render_template,url_for,redirect,request,session,flash

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
      flash("Login successfull")
      return redirect(url_for("user"))   
    else:
       if "res" in session:
         flash("Already Loggedin")
         redirect(url_for("user"))
       return render_template("login.html")

@app.route("/user")
def user():
    if "many" in session:
        res=session["many"]
        return render_template("user.html",res=res)
    else:
        flash("You are loggedin!")
        return redirect(url_for("login"))
@app.route("/logout")
def logout():
    session.pop("many",None)
    flash("you have been logged out,{res}","info")
    return redirect(url_for("login"))
if __name__=='__main__':
    app.run(debug=True)
