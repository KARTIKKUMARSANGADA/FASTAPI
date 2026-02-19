from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from database import Base, engine, get_db
from models import BookTable, StudentTable
from schemas import BookSchema

# Create tables from models
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Library Management API",
              description="You can manage books")


@app.get("/greet/{name}", tags=["Librarian"])
def greeting(name: str):
    return {"message": f"{name}, welcome to Library"}


@app.get("/student_data/{id}", tags=["Librarian"])
def get_student_data(id: int, db: Session = Depends(get_db)):
    student = db.query(StudentTable).filter(StudentTable.id == id).first()
    if student is None:
        raise HTTPException(status_code=404, detail="Student not found")
    return student


@app.get("/student_details", tags=["Librarian"])
def students_details(db: Session = Depends(get_db)):
    return db.query(StudentTable).all()


@app.post("/add", tags=["Librarian"])
def add_book(book: BookSchema, db: Session = Depends(get_db)):
    new_book = BookTable(**book.model_dump())
    db.add(new_book)
    db.commit()
    db.refresh(new_book)
    return {"message": "Book added successfully", "book_id": new_book.id}


@app.get("/book_details", tags=["Librarian"])
def all_books(db: Session = Depends(get_db)):
    return db.query(BookTable).all()


@app.put("/update/{id}", tags=["Librarian"])
def update_book(id: int, book: BookSchema, db: Session = Depends(get_db)):
    existing = db.query(BookTable).filter(BookTable.id == id).first()
    if existing is None:
        raise HTTPException(status_code=404, detail="Book not found")

    existing.title = book.title
    existing.author = book.author
    db.commit()
    db.refresh(existing)
    return {"message": "Book updated successfully", "book": existing}


@app.delete("/delete/{id}", tags=["Librarian"])
def delete_book(id: int, db: Session = Depends(get_db)):
    book = db.query(BookTable).filter(BookTable.id == id).first()
    if book is None:
        raise HTTPException(status_code=404, detail="Book not found")

    db.delete(book)
    db.commit()
    return {"message": "Book deleted"}


@app.get("/students/{id}", tags=["Student"])
def get_student_by_id(id: int, db: Session = Depends(get_db)):
    student = db.query(StudentTable).filter(StudentTable.id == id).first()
    if student is None:
        raise HTTPException(status_code=404, detail="Student not found")
    return student


@app.get("/available_books", tags=["Student"])
def available_books(db: Session = Depends(get_db)):
    return db.query(BookTable).all()


@app.post("/borrow_book/{id}", tags=["Student"])
def borrow_book(id: int, student_name: str, db: Session = Depends(get_db)):
    book = db.query(BookTable).filter(BookTable.id == id).first()
    if book is None:
        raise HTTPException(status_code=404, detail="You cannot borrow this book")

    borrowed = StudentTable(name=student_name, title=book.title)
    db.add(borrowed)
    db.delete(book)
    db.commit()
    return {"message": "Book borrowed successfully"}


@app.post("/deposit_book/{name}", tags=["Student"])
def deposit_book(name: str, db: Session = Depends(get_db)):
    borrowed_row = db.query(StudentTable).filter(StudentTable.name == name).first()
    if borrowed_row is None:
        raise HTTPException(status_code=404, detail="You cannot deposit book")

    restored_book = BookTable(title=borrowed_row.title, author="Unknown")
    db.add(restored_book)
    db.delete(borrowed_row)
    db.commit()
    return {"message": "Book deposited successfully"}
