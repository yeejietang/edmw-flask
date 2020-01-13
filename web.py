from flask import Flask, flash, redirect, render_template, request, session, abort
app = Flask(__name__)

@app.route("/")
def index():
	return render_template("home.html")

@app.route("/hello")
def hello():
	return "Hello"

@app.route("/hello/<string:name>/")
def say_hi(name):
	return "Hello " + name + "!"

if __name__ == "__main__":
	app.run()