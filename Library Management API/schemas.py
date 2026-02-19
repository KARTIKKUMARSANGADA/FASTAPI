from pydantic import BaseModel


class BookSchema(BaseModel):
    title: str
    author: str


class StudentBorrowSchema(BaseModel):
    student_name: str
    book_name : str
