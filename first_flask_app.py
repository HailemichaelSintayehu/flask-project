from flask import Flask,render_template,url_for,redirect   

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html",content={'time':'zara','joe':7,'bill':'first'})

if __name__=='__main__':
    app.run(debug=True)

  