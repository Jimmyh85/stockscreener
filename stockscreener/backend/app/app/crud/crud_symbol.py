from typing import List

from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session

from app.crud.base import CRUDBase
from app.models.symbol import Symbol
from app.schemas.symbol import SymbolCreate, SymbolUpdate


class CRUDSymbol(CRUDBase[Symbol, SymbolCreate, SymbolUpdate]):
    pass


symbol = CRUDSymbol(Symbol)
