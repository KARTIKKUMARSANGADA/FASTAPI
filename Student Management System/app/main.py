from fastapi import FastAPI

from app.database import engine ,Base
from app.routers import auth, student, course, enrollments,grade
import app.models  # noqa: F401  (ensure model metadata is imported)

Base.metadata.create_all(bind=engine)
app = FastAPI(title="Student Management System") 


@app.get("/",tags=['Welcome'])
def welcome():
    return {"message": "Welcome TO Student Management System"}


app.include_router(auth.router)
app.include_router(student.router)
app.include_router(course.router)
app.include_router(enrollments.router)
app.include_router(grade.router)


