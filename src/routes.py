from flask import render_template, Blueprint

main = Blueprint('main', __name__, url_prefix='/')


@main.route("/")
def home_page():
    print("Entered home page")
    return render_template("home.html")

@main.route("/aka")
def page():
    print("Entered page")
    return render_template("aka.html")
