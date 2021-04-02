from datetime import datetime
from typing import Optional

from pydantic import BaseModel


# Shared properties
class StockCategoryBase(BaseModel):
    name: str


# Properties to receive on item creation
class StockCategoryCreate(StockCategoryBase):
    pass


# Properties to receive on item update
class StockCategoryUpdate(StockCategoryBase):
    pass


# Properties shared by models stored in DB
class StockCategoryInDBBase(StockCategoryBase):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True


# Additional properties to return to client
class StockCategory(StockCategoryInDBBase):
    pass


# Additional properties stored in DB
class StockCategoryInDB(StockCategoryInDBBase):
    pass
