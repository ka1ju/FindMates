from flask import *
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired

app = Flask('__name__')
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')


class RegisterForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Register')


@app.route('/')
def main():
    return render_template('start.html')


@app.route('/news')
def news():
    return render_template('start.html')


@app.route('/my_mates')
def my_mates():
    return render_template('my_mates.html')


@app.route('/find_mates')
def find_mates():
    return render_template('find_mates.html')


@app.route('/profiles')
def profiles():
    return render_template('profiles.html')


@app.route('/register')
def register():
    return render_template('register.html')


@app.route('/test')
def meme():
    login_form = LoginForm()
    register_form = RegisterForm()
    if login_form.validate_on_submit():
        return redirect('/success')
    elif register_form.validate_on_submit():
        return redirect('/register')
    return render_template('test.html', title="Test", login_form=login_form, register_form=register_form)


if __name__ == '__main__':
    app.run(port='8080', host='127.0.0.1')
