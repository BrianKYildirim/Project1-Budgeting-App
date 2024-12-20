from flask import Blueprint, render_template

auth = Blueprint('auth', __name__)

@auth.route('/login.html', methods=['GET', 'POST'])
def login():
    return render_template("login.html")

@auth.route('/logout', methods=['GET', 'POST'])
def logout():
    return "<p>Logout</p>"

@auth.route('/signup.html', methods=['GET', 'POST'])
def sign_up():
    return render_template("signup.html")