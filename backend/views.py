from flask import Blueprint, render_template, request
views = Blueprint(__name__,"views")

@views.route("/")
def home():
    return render_template("index.html",name="loda")

@views.route("/profile")
def profile():
    args = request.args
    name = args.get('name')
    
    return render_template("index.html",name = name)