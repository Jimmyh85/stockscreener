from typing import Any, List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import crud, models, schemas
from app.api import deps

router = APIRouter()


@router.get("/", response_model=List[schemas.Symbol])
def read_symbols(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Retrieve symbols.
    """
    symbols = crud.symbol.get_multi(db, skip=skip, limit=limit)
    return symbols


@router.post("/", response_model=schemas.Symbol)
def create_symbol(
    *,
    db: Session = Depends(deps.get_db),
    item_in: schemas.SymbolCreate,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Create new item.
    """
    symbol = crud.symbol.create(db=db, obj_in=item_in)
    return symbol
