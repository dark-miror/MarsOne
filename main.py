from datetime import datetime as dt

from flask import Flask, render_template, redirect, request, make_response, session
from flask_login import LoginManager, login_user, login_required, logout_user, current_user

from data import db_session
from data.jobs import Jobs
from data.users import User

from forms.register import RegisterForm
from forms.login import LoginForm

app = Flask(__name__)
login_manager = LoginManager()
login_manager.init_app(app)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


def clear_table(table):
    db_sess = db_session.create_session()
    db_sess.query(table).filter().delete()
    db_sess.commit()


def new_person(surname, name, age, position, speciality, address, email):
    user = User()
    user.surname = surname
    user.name = name
    user.age = age
    user.position = position
    user.speciality = speciality
    user.address = address
    user.email = email

    db_sess = db_session.create_session()
    db_sess.add(user)
    db_sess.commit()


def new_job(team_leader, job, work_size, collaborators, start_date=dt.now(), is_finished=False):
    jobs = Jobs()
    jobs.team_leader = team_leader
    jobs.job = job
    jobs.work_size = work_size
    jobs.collaborators = collaborators
    jobs.start_date = start_date
    jobs.is_finished = is_finished

    db_sess = db_session.create_session()
    db_sess.add(jobs)
    db_sess.commit()


def main():
    db_session.global_init("db/mars.db")
    app.run()


@login_manager.user_loader
def load_user(user_id):
    db_sess = db_session.create_session()
    return db_sess.query(User).get(user_id)


@app.route("/")
def index():
    db_sess = db_session.create_session()
    jobs = db_sess.query(Jobs).all()
    return render_template("index.html", jobs=jobs)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        user = db_sess.query(User).filter(User.email == form.email.data).first()
        if user and user.check_password(form.password.data):
            login_user(user, remember=form.remember_me.data)
            return redirect("/")
        return render_template('login.html',
                               message="Неправильный логин или пароль",
                               form=form)
    return render_template('login.html', title='Авторизация', form=form)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect("/")


@app.route('/register', methods=['GET', 'POST'])
def reqister():
    form = RegisterForm()
    if form.validate_on_submit():
        if form.password.data != form.password_again.data:
            return render_template('register.html', form=form, message="Пароли не совпадают")
        db_sess = db_session.create_session()
        if db_sess.query(User).filter(User.email == form.email.data).first():
            return render_template('register.html', form=form,
                                   message="Такой пользователь уже есть")
        user = User(
            surname=form.surname.data,
            name=form.name.data,
            age=form.age.data,
            position=form.position.data,
            speciality=form.speciality.data,
            address=form.address.data,
            email=form.email.data
        )
        user.set_password(form.password.data)
        db_sess.add(user)
        db_sess.commit()
        return redirect('/login')
    return render_template('register.html', form=form)


if __name__ == '__main__':
    main()
