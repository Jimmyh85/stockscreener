from typing import Optional

from datetime import datetime
from pydantic import BaseModel


# Shared properties
class ExchangeBase(BaseModel):
    abbrev: str
    name: str
    city: Optional[str] = None
    country: Optional[str] = None
    currency: Optional[str] = None


# Properties to receive on item creation
class ExchangeCreate(ExchangeBase):
    pass


# Properties to receive on item update
class ExchangeUpdate(ExchangeBase):
    pass


# Properties shared by models stored in DB
class ExchangeInDBBase(ExchangeBase):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True


# Properties to return to client
class Exchange(ExchangeInDBBase):
    pass


# Properties properties stored in DB
class ExchangeInDB(ExchangeInDBBase):
    pass
