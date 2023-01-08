from flask import Flask, render_template, request, flash, redirect

app = Flask(__name__)
app.secret_key = "sladklaskdksa"


@app.route("/hello")
def index():
    flash("What's your name?")
    return render_template("index.html")


@app.route("/greet", methods=["GET", "POST"])
def greet():
    name = str(request.form["name_input"])
    if len(name) == 0:
        print('vazio')
        return redirect('/hello')
    else:
        flash("Hi " + name + "! great to see you! :)")
        return render_template("index.html")
