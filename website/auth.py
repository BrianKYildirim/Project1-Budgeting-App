from flask import Blueprint, render_template, request, flash

auth = Blueprint('auth', __name__)

@auth.route('/login.html', methods=['GET', 'POST'])
def login():
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
        username = request.form.get('username')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        num = False
        upperCase = False
        special = False

        for char in password1:
            if char.isdigit():
                num = True
            if char.isupper():
                upperCase = True
            if not char.isalnum():
                special = True

        if len(email) < 4:
            flash("Email must be at least 4 characters.", category="Error")
        elif len(username) < 2:
            flash("First name must be at least 2 characters.", category="Error")
        elif password1 != password2:
            flash("Passwords do not match.", category="Error")
        elif len(password1) < 8:
            flash("Password must be at least 8 characters.", category="Error")
        elif not num or not upperCase or not special:
            flash(
                "Password must include at least one uppercase letter, one number, and one symbol.",
                category="Error")
        else:
            flash("Account created!", category="Success")

    return render_template("signup.html")