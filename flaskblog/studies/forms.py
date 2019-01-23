from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, SelectField
from wtforms.validators import DataRequired

choices = [(1, 'Opening'), (2, 'Middlegame'), (3, 'Endgame'), (4, 'Match')]
class StudyForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    content = TextAreaField('Content', validators=[DataRequired()])
    category = SelectField('Category', choices = choices, validators = [], coerce=int)
    board = StringField('Embeded board', validators=[DataRequired()])
    submit = SubmitField('Add game')
