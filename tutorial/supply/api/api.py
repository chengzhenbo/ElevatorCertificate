from fastapi import APIRouter

from api.endpoints import (supplier_board,
                           supplier_ropehead)

api_router = APIRouter()
api_router.include_router(supplier_board.router, 
                          prefix="/supplier/board", tags=["supplier board"])
api_router.include_router(supplier_ropehead.router, 
                          prefix="/supplier/ropehead", tags=["supplier ropehead"])