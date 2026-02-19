from sqlalchemy import Column, Integer, String

from database import Base


class BookTable(Base):
    __tablename__ = "LibraryDB"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    author = Column(String, nullable=False)


class StudentTable(Base):
    __tablename__ = "StudentDB"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    title = Column(String, nullable=False)
