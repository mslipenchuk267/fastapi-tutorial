from pydantic import BaseModel

class ItemBase(BaseModel):
    text: str
    is_done: bool = False

class ItemCreate(ItemBase):
    pass

class Item(ItemBase):
    id: int = None

    class Config:
        from_attributes = True