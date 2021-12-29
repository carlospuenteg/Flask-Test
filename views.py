from flask import Blueprint, render_template, request, jsonify, redirect, url_for

views = Blueprint(__name__, "views")

@views.route("/")
def home():
    return render_template("index.html", name="Joe") # , age="21"
'''
@views.route("/profile")
def profile():
    args = request.args
    name = args.get("name") 
    return render_template("index.html", name=name) # http://127.0.0.1:8000/views/profile?name=Billy
'''
'''
@views.route("/profile/<username>")
def profile(username):
    return render_template("index.html", name=username) # http://127.0.0.1:8000/views/profile/Tim
'''

@views.route("/json")
def get_json():
    return jsonify({"name": "tim", "coolness": 10}) # http://127.0.0.1:8000/views/json

@views.route("/data")
def get_data():
    data = request.json
    return jsonify(data)

@views.route("/go-to-json")
def go_to_json():
    return redirect(url_for("views.get_json"))

@views.route("/profile")
def profile():
    return render_template("profile.html") # http://127.0.0.1:8000/views/profile?name=Billy