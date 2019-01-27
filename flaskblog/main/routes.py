from flask import Blueprint
from flask import render_template, request, Blueprint
from flaskblog.models import Post

main = Blueprint('main', __name__)


@main.route("/")
def welcome():
    return render_template('welcome.html')


@main.route("/home")
def home():
    page = request.args.get('page', 1, type=int)
    posts = Post.query.order_by(Post.date_posted.desc()).paginate(page = page, per_page=3)
    return render_template('home.html', posts = posts)


@main.route("/about")
def about():
    return render_template('about.html')



@main.route("/503")
def about2():
    return render_template('errors/503.html')
