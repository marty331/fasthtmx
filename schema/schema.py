from typing import List

from pydantic import BaseModel


class BookBase(BaseModel):
    title: str
    pages: int
    author_id: int


class CreateBook(BookBase):
    pass


class Book(BookBase):
    id: str

    class Config:
        orm_mode = True


class AuthorBase(BaseModel):
    first_name: str
    last_name: str
    email: str


class AuthorCreate(AuthorBase):
    pass


class Author(AuthorBase):
    id: int
    books: List[Book] = []

    class Config:
        orm_mode = True
