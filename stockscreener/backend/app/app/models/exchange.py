from typing import TYPE_CHECKING

from sqlalchemy import Column, ForeignKey, Integer, String, DateTime, Time, TIMESTAMP
from sqlalchemy.orm import relationship
from sqlalchemy.sql.expression import func

from app.db.base_class import Base

# if TYPE_CHECKING:
#     from .user import User  # noqa: F401


class Exchange(Base):
    id = Column(Integer, primary_key=True, index=True)
    abbrev = Column(String, unique=True, nullable=False)
    name = Column(String, index=True)
    city = Column(String)
    country = Column(String)
    currency = Column(String)
    timezone_offset = Column(Time)
    created_at = Column(TIMESTAMP, default=func.now())
    updated_at = Column(TIMESTAMP, default=func.now(), onupdate=func.now())
