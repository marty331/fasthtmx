from typing import Optional

from sqlalchemy.orm import Session

from viewmodels.shared.viewmodelbase import ViewModelBase
from services import db_service as dbs


class AddBookViewModel(ViewModelBase):
    def __init__(self, db: Session):
        super().__init__()

        self.author_id: Optional[int] = None
        self.id: Optional[int] = None
        self.title: Optional[str] = None
        self.pages: Optional[int] = None
        self.db = db
        self.authors = dbs.get_authors(db)

    def restore_from_form(self):
        d = self.request_dict
        self.title = d.get('title')
        self.pages = d.get('pages')
        self.id = d.get('id')
        self.author_id = d.get('author_id')
