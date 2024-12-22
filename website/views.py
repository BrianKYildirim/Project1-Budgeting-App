from flask import Blueprint, render_template
from flask_login import login_required, current_user

views = Blueprint('views', __name__)

@views.route('/')
def index():
    return render_template("index.html")

@views.route('/dashboard.html')
@login_required
def dashboard():
    return render_template("dashboard.html", user=current_user)

@views.route('/budgets.html')
def budgets():
    return render_template("budgets.html")

@views.route('/insights.html')
def insights():
    return render_template("insights.html")
