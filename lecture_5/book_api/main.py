from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from database import Base, engine, SessionLocal
import models
import schemas

Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        
@app.post("/books/", response_model=schemas.Book)
def create_book(book: schemas.BookCreate, db: Session = Depends(get_db)):
    db_book = models.Book(**book.dict())
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book

@app.get("/books/", response_model=list[schemas.Book])
def get_books(db: Session = Depends(get_db)):
    return db.query(models.Book).all()

@app.delete("/books/{book_id}")
def delete_book(book_id: int, db: Session = Depends(get_db)):
    book = db.query(models.Book).filter(models.Book.id == book_id).first()
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    db.delete(book)
    db.commit()
    return {"message": "Book deleted"}

@app.put("/books/{book_id}", response_model=schemas.Book)
def update_book(book_id: int, data: schemas.BookCreate, db: Session = Depends(get_db)):
    book = db.query(models.Book).filter(models.Book.id == book_id).first()
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    
    book.title = data.title
    book.author = data.author
    book.year = data.year
    db.commit()
    db.refresh(book)
    return book

@app.get("/books/search/", response_model=list[schemas.Book])
def search_books(title: str = None, author: str = None, year: int = None, db: Session = Depends(get_db)):
    query = db.query(models.Book)
    if title:
        query = query.filter(models.Book.title.contains(title))
    if author:
        query = query.filter(models.Book.author.contains(author))
    if year:
        query = query.filter(models.Book.year == year)
    return query.all()