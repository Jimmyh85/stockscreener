from typing import TYPE_CHECKING

from sqlalchemy import Boolean, Column, Integer, String, DateTime, ForeignKey, TIMESTAMP
from sqlalchemy.orm import relationship
from sqlalchemy.sql.expression import func

from app.db.base_class import Base

# from sqlalchemy.sql.sqltypes import TIMESTAMP

if TYPE_CHECKING:
    from .exchange import Exchange  # noqa: F401
    from .stock_index import StockIndex  # noqa: F401
    from .stock_category import StockCategory  # noqa: F401


class Symbol(Base):
    id = Column(Integer, primary_key=True, index=True)
    exchange_id = Column(Integer, ForeignKey("exchange.id"))
    ticker = Column(String, unique=True, index=True, nullable=False)
    instrument = Column(String, nullable=False)
    name = Column(String)
    stock_index_id = Column(Integer, ForeignKey("stock_index.id"))
    stock_category_id = Column(Integer, ForeignKey("stock_category.id"))
    sector = Column(String)
    currency = Column(String)
    created_at = Column(TIMESTAMP, default=func.now())
    updated_at = Column(TIMESTAMP, default=func.now(), onupdate=func.now())
