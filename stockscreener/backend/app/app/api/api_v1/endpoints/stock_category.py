from typing import Any, List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import crud, models, schemas
from app.api import deps

router = APIRouter()


@router.get("/", response_model=List[schemas.StockCategory])
def read_symbols(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Retrieve symbols.
    """
    categories = crud.stock_category.get_multi(db, skip=skip, limit=limit)
    return categories


@router.post("/", response_model=schemas.StockCategory)
def create_symbol(
    *,
    db: Session = Depends(deps.get_db),
    item_in: schemas.StockCategoryCreate,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Create new item.
    """
    category = crud.stock_category.create(db=db, obj_in=item_in)
    return category
