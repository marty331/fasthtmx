from typing import Optional

from sqlalchemy.orm import Session

from viewmodels.shared.viewmodelbase import ViewModelBase


class AddAuthorViewModel(ViewModelBase):
    def __init__(self):
        super().__init__()

        self.first_name: Optional[str] = None
        self.last_name: Optional[int] = None
        self.email: Optional[str] = None

    def restore_from_form(self):
        d = self.request_dict
        self.first_name = d.get('first_name')
        self.last_name = d.get('last_name')
        self.email = d.get('email')
