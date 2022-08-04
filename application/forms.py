from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, TextAreaField
from wtforms.validators import DataRequired



class ReaderForm(FlaskForm):
    forename = StringField('Enter Forename', validators=[DataRequired()])
    surname = StringField('Enter Surname', validators=[DataRequired()])
    submit = SubmitField('Enter')


class BookForm(FlaskForm):
    book_title = StringField('Book Title', validators=[DataRequired()])
    book_author = StringField('Author', validators=[DataRequired()])
    book_length = StringField('Book Length', validators=[DataRequired()])
    book_desc = TextAreaField('Brief Description', validators=[DataRequired()])
    year_published = StringField('Publication Year', validators=[DataRequired()])
    read_by = SelectField('Read by', choices=[])
    submit = SubmitField('Enter')