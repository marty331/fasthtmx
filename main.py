from fastapi import FastAPI, Depends, HTTPException, Request, Form
from fastapi.responses import RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session

from db.database import SessionLocal, engine
from schema import schema
from models import models
from services import db_service as dbs

from viewmodels.books import addbookviewmodel, showbooks, searchbooks
from viewmodels.authors import showauthors, authorbooks
from viewmodels.home import homeviewmodel


models.Base.metadata.create_all(bind=engine)

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
def home_page(request: Request, db: Session = Depends((get_db))):
    vm = homeviewmodel.HomeViewModel(db=db)
    books = vm.books
    return templates.TemplateResponse('home/index.html', {"request": request, "books": books})


@app.get("/author/add")
def authors_add(request: Request):
    return templates.TemplateResponse('authors/partials/add_authors_form.html', {"request": request})


@app.post("/authors/add")
def create_author(request: Request, email: str = Form(...), first_name: str = Form(...), last_name: str = Form(...), db: Session = Depends(get_db)):
    db_author = dbs.get_author_by_email(db, email=email)
    if db_author:
        raise HTTPException(status_code=400, detail="Email already registered")
    author = schema.AuthorCreate(last_name=last_name, first_name=first_name, email=email)
    dbs.create_author(db=db, author=author)
    url = request.headers.get('HX-Current-URL').split('/')[-1]
    if request.headers.get('HX-Request') and url == 'authors':
        return templates.TemplateResponse('authors/partials/show_add_author_form.html', {"request": request})
    elif request.headers.get('HX-Request') and url == '':
        return templates.TemplateResponse('books/partials/show_add_form.html', {"request": request})
    else:
        pass
    return RedirectResponse(url="/", status_code=302)


@app.get("/authors/cancel_add")
def cancel_author(request: Request):
    url = request.headers.get('HX-Current-URL').split('/')[-1]
    if url == 'authors':
        return templates.TemplateResponse('authors/partials/show_add_author_form.html', {"request": request})
    return templates.TemplateResponse('books/partials/show_add_form.html', {"request": request})


@app.get("/authors/close_books/{author_id}")
def close_authors_books(request: Request, author_id: int):
    return templates.TemplateResponse('authors/partials/show_books.html', {"request": request, "author_id": author_id})


@app.get("/authors")
def show_authors(request: Request, db: Session = Depends(get_db)):
    vm = showauthors.ShowAuthorsViewModel(db=db)
    authors = vm.authors
    return templates.TemplateResponse('authors/authors.html', {"request": request, "authors": authors})


@app.get("/author/books/{author_id}")
def authors_books(request: Request, author_id: int, db: Session = Depends(get_db)):
    vm = authorbooks.AuthorBooksViewModel(db=db, author_id=author_id)
    books = vm.books
    return templates.TemplateResponse('authors/partials/authors_books.html',
                                      {"request": request, "books": books, "author_id": author_id})


@app.get("/books/add")
def add_book(request: Request, db: Session = Depends(get_db)):
    vm = addbookviewmodel.AddBookViewModel(db=db)
    data = vm.to_dict()
    return templates.TemplateResponse('books/partials/add_books_form.html', {"request": request, "data": data})


@app.post("/books/add")
def book_add(title: str = Form(...), pages: str = Form(...), author_id: str = Form(...), db: Session = Depends(get_db)):
    db_book = dbs.get_book(db, title=title)
    if db_book:
        raise HTTPException(status_code=400, detail="Book already exists.")
    book = schema.CreateBook
    book.title = title
    book.author_id = int(author_id)
    book.pages = int(pages)
    dbs.create_book(db, book=book)
    return RedirectResponse(url="/", status_code=302)


@app.get("/books/cancel_add")
def cancel_add(request: Request):
    return templates.TemplateResponse('books/partials/show_add_form.html', {"request": request})


@app.get("/books")
def get_books(request: Request, db: Session = Depends(get_db)):
    vm = showbooks.ShowBooksViewModel(db=db)
    books = vm.books
    return templates.TemplateResponse('books/books.html', {"request": request, "books": books, "search_text": ""})


@app.get("/books/search")
def search_books(request: Request, search_text: str, db: Session = Depends(get_db)):
    vm = searchbooks.SearchViewModel(db=db, search_text=search_text)
    if request.headers.get('HX-Request'):
        return templates.TemplateResponse("books/partials/search_results.html", {"request": request, "books": vm.books})
    return templates.TemplateResponse('books/books.html', {"request": request, "books": vm.books, "search_text": search_text})
