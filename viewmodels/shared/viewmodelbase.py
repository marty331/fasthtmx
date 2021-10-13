from typing import Optional

import fastapi
from fastapi import Request


class ViewModelBase:
    def __init__(self):
        self.request: Request = fastapi.requests
        self.error: Optional[str] = None
        self.view_model = self.to_dict()

    def to_dict(self):
        return self.__dict__
