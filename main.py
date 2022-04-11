import os
from flask import *
from flask_login import LoginManager, login_user, current_user, logout_user
from data import db_session
from data.news import News
from data.users import User
from forms.user import *

app = Flask('__name__')
app.config['SECRET_KEY'] = 'yandex_lyceum_secret_key'

login_manager = LoginManager()
login_manager.init_app(app)


@app.route('/')
def main():
    return redirect('/news')


@app.route('/news')
def news():
    db_sess = db_session.create_session()
    users = db_sess.query(User)
    n = db_sess.query(News)
    n = list(n)
    n.reverse()
    return render_template("news.html", users=users, news=n)


@app.route('/find_mates')
def find_mates():
    db_sess = db_session.create_session()
    users = db_sess.query(User)
    return render_template('find_mates.html', users=users)


@app.route('/register', methods=['GET', 'POST'])
def r():
    form = RegisterForm()
    if form.validate_on_submit():
        if form.password.data != form.password_again.data:
            return render_template('register.html', form=form, message="Passwords don't match")
        db_sess = db_session.create_session()
        if db_sess.query(User).filter(User.username == form.name.data).first():
            return render_template('register.html', form=form,
                                   message="Current user is already registered")
        user = User(username=form.name.data, discord=form.discord.data, competitive_rank="1", wingman_rank="1",
                    faceit_level=1, steam=form.steam.data, is_active=True)
        user.set_password(form.password.data)
        db_sess.add(user)
        db_sess.commit()
        return redirect('/login')
    return render_template('register.html', form=form)


@login_manager.user_loader
def load_user(user_id):
    db_sess = db_session.create_session()
    return db_sess.query(User).get(user_id)


@app.route('/login', methods=['GET', 'POST'])
def login():
    print(current_user.is_authenticated)
    form = LoginForm()
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        user = db_sess.query(User).filter(User.username == form.username.data).first()
        if user and user.check_password(form.password.data):
            login_user(user, remember=form.remember_me.data)
            return redirect("/")
        return render_template('login.html',
                               message="Wrong login or password",
                               form=form)
    return render_template('login.html', form=form)


@app.route('/exit')
def left():
    print('exit')
    logout_user()
    return redirect('/')


@app.route('/create_news', methods=['GET', 'POST'])
def create_news():
    form = NewsForm()
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        n = News(title=form.title.data, content=form.content.data, user_id=current_user.id)
        db_sess.add(n)
        db_sess.commit()
        return redirect('/')
    return render_template('create_news.html', form=form)


if __name__ == '__main__':
    db_session.global_init("db/my-mates.sqlite")
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
