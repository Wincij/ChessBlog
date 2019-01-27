from flask import (render_template, url_for, flash,
                   redirect, request, abort, Blueprint)
from flask_login import current_user, login_required
from flaskblog import db
from flaskblog.models import Study
from flaskblog.studies.forms import StudyForm


studies_blueprint = Blueprint('studies', __name__)


@studies_blueprint.route("/study/new", methods=['GET', 'POST'])
@login_required
def new_study():
    form = StudyForm()
    if form.validate_on_submit():
        db.create_all()
        study = Study(title=form.title.data, content=form.content.data, board=form.board.data, category=form.category.data, user_id=current_user.id)
        print(type(form.category.data))
        db.session.add(study)
        db.session.commit()
        flash('Your study has been created!', 'success')
        return redirect(url_for('main.home'))
    return render_template('create_study.html', title='New Study',
                           form=form, legend='New Study')

# @studies_blueprint.route("/study/<string:study_name>/update", methods=['GET', 'POST'])
# @login_required
# def update_study(study_name):
#     study = Study.query.get_or_404(post_id)
#     if post.author != current_user:
#         abort(403)
#     form = PostForm()
#     if form.validate_on_submit():
#         post.title = form.title.data
#         post.content = form.content.data
#         db.session.commit()
#         flash('Your post has been updated!', 'success')
#         return redirect(url_for('posts.post', post_id=post.id))
#     elif request.method == 'GET':
#         form.title.data = post.title
#         form.content.data = post.content
#     return render_template('create_post.html', title='Update Post',
#                            form=form, legend='Update Post')


@studies_blueprint.route("/study")
def studies():
    category1  = Study.query.filter(Study.category == 1).order_by(Study.id.desc())


    return render_template('studies.html', category1 = category1)




@studies_blueprint.route("/study/openings")
def openings():
    # page = request.args.get('page', 1, type=int)
    # posts = Study.query.order_by(Post.date_posted.desc()).paginate(page = page, per_page=3)
    studies = Study.query.filter(Study.category == 1)
    return render_template('opening.html', studies = studies)




@studies_blueprint.route("/study/middlegames")
def middlegames():
    return render_template('middlegame.html')




@studies_blueprint.route("/study/endgames")
def endgames():
    return render_template('endgame.html')



@studies_blueprint.route("/study/matches")
def matches():
    return render_template('matches.html')
