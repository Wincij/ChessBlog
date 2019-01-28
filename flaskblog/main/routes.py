from flask import Blueprint
from flask import render_template, request, Blueprint
from flaskblog.models import Post
from random import randint


main = Blueprint('main', __name__)



maxims = ["“I am convinced, the way one plays chess always reflects the player’s personality. If something defines his character, then it will also define his way of playing.” – Vladimir Kramnik",
        "“The game of chess is not merely an idle amusement. Several very valuable qualities of the mind, useful in the course of human life, are to be acquired or strengthened by it… Life is a kind of Chess, in which we have often points to gain, and competitors or adversaries to contend with.” – Benjamin Franklin",
        "“As proved by evidence, [chess is] more lasting in its being and presence than all books and achievements; the only game that belongs to all people and all ages; of which none knows the divinity that bestowed it on the world, to slay boredom, to sharpen the senses, to exhilarate the spirit.” – Stefan Zweig",
        "“Chess doesn’t drive people mad, it keeps mad people sane.” – Bill Hartston",
        "“In life, as in chess, one’s own pawns block one’s way.  A man’s very wealthy, ease, leisure, children, books, which should help him to win, more often checkmate him.” – Charles Buxton",
        "“Chess is life in miniature. Chess is a struggle, chess battles.” – Garry Kasparov",
        "“Chess, like love, like music, has the power to make men happy.” – Siegbert Tarrasch",
        "“For in the idea of chess and the development of the chess mind we have a picture of the intellectual struggle of mankind.” – Richard Réti"
        ]


@main.route("/")
def welcome():
    return render_template('welcome.html')


@main.route("/home")
def home():
    page = request.args.get('page', 1, type=int)
    __random__ = randint(0, 7)
    posts = Post.query.order_by(Post.date_posted.desc()).paginate(page = page, per_page=3)
    return render_template('home.html', posts = posts, quote = maxims[__random__])


@main.route("/about")
def about():
    return render_template('about.html')
