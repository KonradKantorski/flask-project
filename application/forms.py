from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, TextAreaField
from wtforms.validators import DataRequired



class ReaderForm(FlaskForm):
    forename = StringField('Enter Forename', validators=[DataRequired()])
    surname = StringField('Enter Surname', validators=[DataRequired()])
    submit = SubmitField('Enter')


class BookForm(FlaskForm):
    book_title = StringField('Book Title')
    book_author = StringField('Author')
    book_length = StringField('Book Length')
    book_desc = TextAreaField('Brief Description')
    year_published = StringField('Publication Year')
    read_by = SelectField('Read by', choices=[])
    submit = SubmitField('Enter')