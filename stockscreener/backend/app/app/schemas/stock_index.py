from datetime import datetime
from typing import Optional
from pydantic import BaseModel


# Shared properties
class StockIndexBase(BaseModel):
    abbrev: str
    name: str


# Properties to receive on item creation
class StockIndexCreate(StockIndexBase):
    pass


# Properties to receive on item update
class StockIndexUpdate(StockIndexBase):
    pass


# Properties shared by models stored in DB
class StockIndexInDBBase(StockIndexBase):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True


# Properties to return to client
class StockIndex(StockIndexInDBBase):
    pass


# Properties properties stored in DB
class StockIndexInDB(StockIndexInDBBase):
    pass
