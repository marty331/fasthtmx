from typing import List

from sqlalchemy.orm import Session

from services import db_service
from schema.schema import Book

from viewmodels.shared.viewmodelbase import ViewModelBase


class AuthorBooksViewModel(ViewModelBase):
    def __init__(self, db: Session, author_id: int):
        super().__init__()
        author = db_service.get_author(db=db, author_id=author_id)
        print(f"author {author}")
        self.books: List[Book] = author.books
        self.author = author
