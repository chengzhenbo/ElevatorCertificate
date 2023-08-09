from fastapi import APIRouter

from api.endpoints import supplier_board

api_router = APIRouter()
api_router.include_router(supplier_board.router, prefix="/supplier/board", tags=["supplier board"])