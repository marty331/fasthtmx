from typing import List

from sqlalchemy.orm import Session

from schema.schema import Author, AuthorCreate, Book, CreateBook
from models import models


def get_author(db: Session, author_id: int):
    return db.query(models.Authors).filter(models.Authors.id == author_id).first()


def get_authors(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Authors).offset(skip).limit(limit).all()


def get_all_authors(db: Session):
    return db.query(models.Authors).all()

def create_author(db: Session, author: AuthorCreate):
    print(f"create author {author}")
    db_author = models.Authors(first_name=author.first_name, last_name=author.last_name, email=author.email)
    db.add(db_author)
    db.commit()
    db.refresh(db_author)
    return db_author


def get_author_by_email(db: Session, email: str):
    return db.query(models.Authors).filter(models.Authors.email == email).first()


def get_book(db: Session, title: str):
    return db.query(models.Books).filter(models.Books.title == title).first()


def create_book(db: Session, book: CreateBook):
    print(f"create book {book}")
    db_book = models.Books(title=book.title, pages=book.pages, author_id=book.author_id)
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book


def list_books(db: Session, skip: int = 0, limit: int = 1000):
    books = db.query(models.Books).offset(skip).limit(limit).all()
    authors = db.query(models.Authors).all()
    for book in books:
        for author in authors:
            if book.author_id == author.id:
                book.author_name = author.first_name + " " + author.last_name
    return books


def search_books(db: Session, search_text: str):
    results: List[Book] = []

    if not search_text or not search_text.strip():
        return results

    for book in list_books(db=db):
        text = f"{book.title} {book.author_name}".lower()
        if search_text in text:
            results.append(book)
    return results
