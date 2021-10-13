from typing import List

from sqlalchemy.orm import Session

from services import db_service
from schema.schema import Book
from viewmodels.shared.viewmodelbase import ViewModelBase


class ShowBooksViewModel(ViewModelBase):
    def __init__(self, db: Session):
        super().__init__()
        self.books: List[Book] = db_service.list_books(db=db, skip=0, limit=1000)
