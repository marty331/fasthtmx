from typing import List

from sqlalchemy.orm import Session

from services import db_service
from schema.schema import Author

from viewmodels.shared.viewmodelbase import ViewModelBase


class ShowAuthorsViewModel(ViewModelBase):
    def __init__(self, db: Session):
        super().__init__()
        self.authors: List[Author] = db_service.get_all_authors(db=db)


