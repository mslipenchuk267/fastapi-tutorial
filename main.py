from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from app import crud, schemas, models

from app.database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def root():
    return {"Hello" : "world2"}

@app.post("/items/", response_model=schemas.Item)
def create_item(item: schemas.Item, db: Session = Depends(get_db)):
    return crud.create_item(db=db, item=item)


@app.get("/items/", response_model=list[schemas.Item])
def get_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_items(db=db, skip=skip, limit=limit)

@app.get("/items/{item_id}/", response_model=schemas.Item)
def get_item(item_id: int, db: Session = Depends(get_db)):
    #if item_id < len(items):
    return crud.get_item_by_id(db=db, item_id=item_id)
    #else:
    #    raise HTTPException(status_code=404, detail=f"Item {item_id} not Found")

