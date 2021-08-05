from flask import Flask, Blueprint, render_template, session, jsonify, redirect, url_for
from .database import Messages

views = Blueprint('views', __name__)

@views.route('/')
@views.route('/home', methods=['GET','POST'])
def home():
    if 'name' in session:
        return render_template("home.html")
    else:
        return redirect(url_for("auth.login"))


@views.route('/logged_user')
def logged_user():
    data = {'name':""}
    if 'name' in session:
        data['name'] = session['name']
        return jsonify(data)
    else:
        return jsonify(data)

@views.route('/get_messages')
def get_messages():
    all_msgs = Messages.query.all()
    response = []
    for msg in all_msgs[-20:]:
        data = {'message':msg.message, 'name':msg.user_name, 'time':str(msg.time).split(".")[0][:-3]}
        response.append(data)
    return jsonify(response)


