from application import app, db 
from flask import request, redirect, url_for, render_template
from application.models import *
from application.forms import *


@app.route('/')
def index():
    return render_template('home.html')


#---------------------------------------------------------- Create Readers

@app.route('/add-reader', methods=['GET', 'POST'])
def create_reader():
    form = ReaderForm()
    if form.validate_on_submit():
        forename = form.forename.data
        surname = form.surname.data
        new_reader = Reader(forename=forename, surname=surname)
        db.session.add(new_reader)
        db.session.commit()
        return redirect(url_for('view_all_readers'))
    return render_template('reader_form.html', form=form)

#---------------------------------------------------------- Read Readers
@app.route('/view-readers')
def view_all_readers():
    readers = Reader.query.order_by(Reader.forename).all()
    return render_template('view_all_readers.html', readers=list(readers))


@app.route('/get-reader-by-id/<int:id>')
def get_reader_by_id(id):
    reader = Reader.query.get(id)
    return render_template('reader_by_id.html', reader=reader)


# ---------------------------------------------------------- Update Readers


@app.route('/update-reader/<int:id>', methods = ['GET', 'POST'])
def update_reader(id):
    reader_to_update = Reader.query.get(id)
    form = ReaderForm()
    if form.validate_on_submit():
        forename, surname = form.forename.data, form.surname.data
        reader_to_update.forename = forename if forename else reader_to_update.forename
        reader_to_update.surname = surname if surname else reader_to_update.surname
        db.session.commit()
        return redirect(url_for('view_all_readers'))
    return render_template('reader_form.html', form=form)

# ---------------------------------------------------------- Delete Readers

@app.route('/delete-reader/<int:id>')
def delete_reader(id):
    reader_to_delete = Reader.query.get(id)
    for book in reader_to_delete.books:
        db.session.delete(book)
    db.session.delete(reader_to_delete)
    db.session.commit()
    return redirect(url_for('view_all_readers'))



# ---------------------------------------------------------- Create Books

@app.route('/add-book', methods=['GET', 'POST'])
def add_new_book():
    form = BookForm()
    readers = Reader.query.all()
    form.read_by.choices = [(reader.rid, f"{reader.forename} {reader.surname}") for reader in readers]
    if form.validate_on_submit():
        b_title = form.book_title.data 
        b_author = form.book_author.data
        b_length = form.book_length.data
        b_desc = form.book_desc.data
        b_year_published = form.year_published.data 
        rid = form.read_by.data
        new_book = Book(book_title=b_title, book_author=b_author, book_length=b_length, book_desc=b_desc, year_published=b_year_published, read_by=rid)
        db.session.add(new_book)
        db.session.commit()
        return redirect(url_for('view_all_books'))
    return render_template('book_form.html', form=form)

#  ---------------------------------------------------------- Read Books

@app.route('/view-books')
def view_all_books():
    books = Book.query.all()
    return render_template('view_all_books.html', entity='Book', books=books)

# ---------------------------------------------------------- Update Books

@app.route('/update-book/<int:id>', methods=['GET', 'POST'])
def update_book(id):
    book_to_update = Book.query.get(id)
    form = BookForm()
    readers = Reader.query.all()
    form.read_by.choices = [(reader.rid, f"{reader.forename} {reader.surname}") for reader in readers]
    if form.validate_on_submit():
        book_to_update.title = form.book_title.data 
        book_to_update.author = form.book_author.data
        book_to_update.length = form.book_length.data
        book_to_update.book_desc = form.book_desc.data
        book_to_update.year_published = form.year_published.data
        db.session.commit()
        return redirect(url_for('view_all_books'))
    form.book_title.data = book_to_update.book_title
    form.book_author.data = book_to_update.book_author
    form.book_length.data = book_to_update.book_length
    form.book_desc.data = book_to_update.book_desc
    form.year_published.data = book_to_update.year_published
    return render_template('book_form.html', form=form)

# ----------------------------------------------------------Delete Books

@app.route('/delete-book/<int:id>')
def delete_book(id):
    book_to_delete = Book.query.get(id)
    db.session.delete(book_to_delete)
    db.session.commit()
    return redirect(url_for('view_all_books'))