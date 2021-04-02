from fastapi import APIRouter

from app.api.api_v1.endpoints import items, login, users, utils, symbols, stock_category

api_router = APIRouter()
api_router.include_router(login.router, tags=["login"])
api_router.include_router(users.router, prefix="/users", tags=["users"])
api_router.include_router(utils.router, prefix="/utils", tags=["utils"])
api_router.include_router(items.router, prefix="/items", tags=["items"])
api_router.include_router(symbols.router, prefix="/symbols", tags=["symbols"])
api_router.include_router(
    stock_category.router, prefix="/stock_category", tags=["stock_category"]
)
