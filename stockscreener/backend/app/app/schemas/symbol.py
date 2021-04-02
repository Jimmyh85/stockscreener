from datetime import datetime
from typing import Optional
from pydantic import BaseModel


# Shared properties
class SymbolBase(BaseModel):
    ticker: str
    instrument: str
    name: str
    exchange_id: int
    stock_index_id: int
    stock_category_id: Optional[int] = None
    sector: Optional[str] = None
    currency: str


# Properties to receive on item creation
class SymbolCreate(SymbolBase):
    pass


# Properties to receive on item update
class SymbolUpdate(SymbolBase):
    pass


# Properties shared by models stored in DB
class SymbolInDBBase(SymbolBase):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True


# Additional properties to return to client
class Symbol(SymbolInDBBase):
    pass


# Additional properties stored in DB
class SymbolInDB(SymbolInDBBase):
    pass
