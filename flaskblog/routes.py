import secrets
import os
from PIL import Image
from flask import render_template, flash, redirect, url_for, request
from flaskblog import app, db, bcrypt
from flaskblog.forms import RegistrationForm, LoginForm, AccountForm, PostForm
from flaskblog.models import Post, User
from flask_login import login_user, current_user, logout_user, login_required


posts = [
    {
        'author': 'Corey Schafer',
        'title': 'Blog Post 1',
        'content': 'Second post contentSecond post contentSecond post contentSecond post contentSecond post contentSecond post contentSecond post contentSecond post contentSecond post contentSecond post contentSecond post contentSecond post contentSecond post contentSecond post contentSecond post contentSecond post contentSecond post contentSecond post contentSecond post contentSecond post contentSecond post contentSecond post contentSecond post contentSecond post contentSecond post contentSecond post contentSecSecond post contentond post contentSecond post contentSecond post contentSecond post contentSecond post contentSecond post contentSecond post contentSecond post contentSecond post contentSecond post contentSecond post contentSecond post contentSecond post contentSecond post contentSecond post contentSecond post contentSecond post contentSecond post contentSecond post contentSecond post contentSecond post contentSecond post contentSecond post contentSecond post contentdfsdsdfssf',
        'date_posted': 'April 20, 2018'
    },
    {
        'author': 'Jane Doe',
        'title': 'Blog Post 2',
        'content': "For those that enjoyed my previous article, Test Your Positional Chess, let’s do it again. It’s fun to follow positional concepts, and it’s also extremely instructive. Please keep in mind that these puzzles aren’t like usual tactical puzzles. You usually won’t have to find the “one and only one” move since the position might offer several reasonable choices. So, if you think you found the right move but the software says nyet, keep trying. Also, this isn’t for 1000-rated players or for masters; it’s for everyone. After all, when you’re playing a serious game you’ll need to deal with the game’s complexity (or lack thereof) whether you like it or not. Anyway, the real goal is to understand the position and THEN and ONLY THEN look for moves that cater to the position’s needs.",
        'date_posted': 'April 21, 2018'
    }
]



@app.route("/")
def welcome():
    return render_template('welcome.html', posts = posts)


@app.route("/home")
def home():
    return render_template('home.html', posts = posts)


@app.route("/about")
def about():
    return render_template('about.html')




@app.route("/register", methods=["GET", "POST"])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username = form.username.data, email = form.email.data, password = hashed_password)
        db.session.add(user)
        db.session.commit()
        flash(f'Your account has been created successfully', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)



@app.route("/login",  methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email = form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember = False)
            return redirect(url_for('home'))
        else:
            flash("Login Unsuccessful", 'danger')
    return render_template('login.html', title='Login', form=form)


def save_picture(form_picture):
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_picture.filename)
    picture_fn = random_hex + f_ext
    picture_path = os.path.join(app.root_path, 'static/profile_pics', picture_fn)

    output_size = (125, 125)
    i = Image.Open(picture_path)
    i.thumbnail(output_size)

    i.save(picture_path)

    return picture_fn


@app.route("/account",  methods=["GET", "POST"])
@login_required
def account():
    image_file = url_for('static', filename = 'profile_pics/' + current_user.image_file)
    form = AccountForm()
    if form.validate_on_submit():
        if form.picture.data:
            picture_file = save_picture(form.picture.data)
            current_user.image_file = picture_file
        current_user.username = form.username.data
        current_user.email = form.email.data
        db.session.commit()
        flash('Your account has been updated', 'success')
        return redirect(url_for('account'))
    elif request.method == 'GET':
        form.username.data = current_user.username
        form.email.data = current_user.email
    return render_template('account.html', image_file = image_file, form = form)





@app.route("/post/new", methods= ['GET', 'POST'])
@login_required
def new_post():
    form = PostForm()
    if form.validate_on_submit():
        flash('Your post has been created', 'success')
        return redirect(url_for('home'))
    return render_template("create_post.html", title='New Post', form = form)





@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('home'))
