from typing import TYPE_CHECKING

from sqlalchemy import (
    Boolean,
    Column,
    Integer,
    String,
    DateTime,
    ForeignKey,
    TIMESTAMP,
    DECIMAL,
    BIGINT,
    UniqueConstraint,
)
from sqlalchemy.orm import relationship
from sqlalchemy.sql.expression import func

from app.db.base_class import Base

# from sqlalchemy.sql.sqltypes import TIMESTAMP

if TYPE_CHECKING:
    from .exchange import Exchange  # noqa: F401
    from .symbol import Symbol  # noqa: F401
    from .stock_category import StockCategory  # noqa: F401


class DailyPrice(Base):
    __tablename__ = "daily_price"

    id = Column(Integer, primary_key=True, index=True)
    symbol_id = Column(Integer, ForeignKey("symbol.id"))
    price_date = Column(TIMESTAMP, nullable=False)
    high_price = Column(DECIMAL, nullable=False)
    open_price = Column(DECIMAL, nullable=False)
    low_price = Column(DECIMAL, nullable=False)
    close_price = Column(DECIMAL, nullable=False)
    adj_close_price = Column(DECIMAL, nullable=False)
    volume = Column(BIGINT, nullable=False)
    created_at = Column(TIMESTAMP, default=func.now())
    updated_at = Column(TIMESTAMP, default=func.now(), onupdate=func.now())

    __table_args__ = (
        UniqueConstraint("symbol_id", "price_date", name="_symbol_price_uc"),
    )
