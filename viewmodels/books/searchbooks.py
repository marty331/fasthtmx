from typing import List

from sqlalchemy.orm import Session

from services import db_service
from schema.schema import Book
from viewmodels.shared.viewmodelbase import ViewModelBase


class SearchViewModel(ViewModelBase):
    def __init__(self, db: Session, search_text: str):
        super().__init__()

        self.books: List[Book] = []
        self.search_text = search_text.strip().lower()

        if self.search_text and self.search_text.strip() and len(self.search_text.strip()) > 1:
            self.books = db_service.search_books(db=db, search_text=self.search_text)
        else:
            self.books = db_service.list_books(db=db)
