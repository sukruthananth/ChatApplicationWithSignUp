from flask import Blueprint, render_template, request,flash, redirect, url_for, session
from . import db
from .database import User
auth = Blueprint('auth', __name__)

@auth.route('/login', methods = ['GET', 'POST'])
def login():
    if 'name' in session:
        return redirect(url_for("views.home"))
    else:
        if request.method == 'POST':
            email = request.form.get('email')
            password = request.form.get('password')
            user = User.query.filter_by(email_id=email).first()
            print(user)
            if user:
                if user.password == password:
                    session['name'] = user.name
                    return redirect(url_for('views.home'))
                else:
                    flash(f'You have entered wrong password ', category='error')
            else:
                flash(f'You have entered wrong email address', category='error')
        return render_template("login.html")

@auth.route("/logout")
def logout():
    session.pop('name', None)
    return redirect(url_for("auth.login"))

@auth.route('/sign-up', methods = ['GET', 'POST'])
def sign_up():
    if 'name' in session:
        return redirect(url_for('views.home'))
    else:
        if request.method == 'POST':
            name = request.form.get('text')
            email = request.form.get('email')
            password = request.form.get('password1')
            email_exists = User.query.filter_by(email_id=email).first()
            if email_exists:
                flash(f'Email already exists!', category='error')
            elif len(request.form.get('text')) < 3:
                flash(f'Name must be more than two characters', category='error')
            elif len(request.form.get('password1')) < 2:
                flash(f'Password must be greater than 7 characters', category='error')
            elif request.form.get('password1') != request.form.get('password2'):
                flash(f'Passwords do not match', category='error')
            else:
                session['name'] = request.form.get('text')
                user = User(email_id=email, name=name, password=password)
                db.session.add(user)
                db.session.commit()
                return redirect(url_for('views.home'))
    return render_template("signup.html")