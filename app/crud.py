from sqlalchemy.orm import Session

from . import schemas

from . import models

def get_items(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Item).offset(skip).limit(limit).all()

def get_item_by_id(db: Session, item_id: int):
    return db.query(models.Item).filter(models.Item.id == item_id).all()

def create_item(db: Session, item: schemas.ItemCreate):
    db_item = models.Item(**item.model_dump()) # equivalent to models.Item(id=None, text='...', is_done=False)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item
