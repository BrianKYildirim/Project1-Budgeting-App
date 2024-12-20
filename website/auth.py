from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db

auth = Blueprint('auth', __name__)

@auth.route('/login.html', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        user = User.query.filter_by(email=email).first()
        if user:
            pass
    data = request.form
    print(data)
    return render_template("login.html")

@auth.route('/logout', methods=['GET', 'POST'])
def logout():
    return "<p>Logout</p>"

@auth.route('/signup.html', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        firstname = request.form.get('firstname')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        num = False
        uppercase = False
        special = False

        for char in password1:
            if char.isdigit():
                num = True
            if char.isupper():
                uppercase = True
            if not char.isalnum():
                special = True

        if not email or not firstname or not password1 or not password2:
            flash('Please fill out all of the fields.', category='Error')
        elif len(email) < 4:
            flash("Email must be at least 4 characters.", category="Error")
        elif len(firstname) < 2:
            flash("First name must be at least 2 characters.", category="Error")
        elif password1 != password2:
            flash("Passwords do not match.", category="Error")
        elif len(password1) < 8:
            flash("Password must be at least 8 characters.", category="Error")
        elif not num or not uppercase or not special:
            flash(
                "Password must include at least one uppercase letter, one number, and one symbol.",
                category="Error")
        else:
            new_user = User(email = email, firstname = firstname, password = generate_password_hash(password1, method='scrypt', salt_length=16))
            db.session.add(new_user)
            db.session.commit()
            flash("Account created!", category="Success")
            return redirect(url_for('views.dashboard'))


    return render_template("signup.html")