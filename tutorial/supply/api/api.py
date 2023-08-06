from fastapi import APIRouter

from api.endpoints import supplier_smart_board

api_router = APIRouter()
api_router.include_router(supplier_smart_board.router, prefix="/supplier", tags=["supplier"])