from flask import Blueprint, render_template

views = Blueprint('views', __name__)

@views.route('/')
def index():
    return render_template("index.html")

@views.route('/dashboard.html')
def dashboard():
    return render_template("dashboard.html")
