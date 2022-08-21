from flask import render_template, flash, redirect, url_for, Response, jsonify
from flask_login import (current_user,
                         login_user,
                         logout_user,
                         login_required)

import celery.states as states
from worker import celery

from app import app, db
from forms import LoginForm, RegistrationForm
from models import User


@app.route('/')
def index():
    return render_template("floorplan.html")


@app.route('/why')
@login_required
def why():
    return render_template("why.html")


@app.route('/add/<int:param1>/<int:param2>')
def add(param1: int, param2: int) -> str:
    task = celery.send_task('tasks.add', args=[param1, param2], kwargs={})
    response = f"<a href='{url_for('check_task', task_id=task.id, external=True)}'>check status of {task.id} </a>"
    return response


@app.route('/check/<string:task_id>')
def check_task(task_id: str) -> str:
    res = celery.AsyncResult(task_id)
    if res.state == states.PENDING:
        return res.state
    else:
        return str(res.result)


@app.route('/health_check')
def health_check() -> Response:
    return jsonify("OK")


@app.route("/user_page")
@login_required
def user_page():
    return render_template('user_page.html')


@app.route('/register', methods=['GET', 'POST'])
def register_user():
    if current_user.is_authenticated:
        flash("Already logged-in")
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)


@app.route("/login", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        flash("Already logged-in")
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        return redirect(url_for('index'))
    return render_template('login.html', form=form)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))


@app.errorhandler(404)
def not_found(error):
    app.logger.debug(error)
    return render_template("error_404.html"), 404


@app.errorhandler(401)
def unauthorized(error):
    app.logger.debug(error)
    return render_template("error_401.html"), 401
