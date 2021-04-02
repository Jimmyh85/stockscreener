from typing import List

from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session

from app.crud.base import CRUDBase
from app.models.stock_category import StockCategory
from app.schemas.stock_category import StockCategoryCreate, StockCategoryUpdate


class CRUDStockCategory(
    CRUDBase[StockCategory, StockCategoryCreate, StockCategoryUpdate]
):
    pass


stock_category = CRUDStockCategory(StockCategory)
