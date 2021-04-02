from datetime import datetime
from typing import Optional
from pydantic import BaseModel


# Shared properties
class DailyPriceBase(BaseModel):
    symbol_id: str
    price_date: datetime
    high_price: float
    open_price: float
    low_price: float
    close_price: float
    adj_close_price: float
    volume: float


# Properties to receive on item creation
class DailyPriceCreate(DailyPriceBase):
    pass


# Properties to receive on item update
class DailyPriceUpdate(DailyPriceBase):
    pass


# Properties shared by models stored in DB
class DailyPriceInDBBase(DailyPriceBase):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True


# Properties to return to client
class DailyPrice(DailyPriceInDBBase):
    pass


# Properties properties stored in DB
class DailyPriceInDB(DailyPriceInDBBase):
    pass
