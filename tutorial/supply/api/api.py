from fastapi import APIRouter

from api.endpoints import (supplier_board,
                           supplier_ropehead,
                           supplier_autorescue,
                           supplier_icard,
                           supplier_safebrake)

api_router = APIRouter()

api_router.include_router(supplier_board.router, 
                          prefix="/supplier/board", 
                          tags=["supplier board 供应商:主板"])
api_router.include_router(supplier_ropehead.router, 
                          prefix="/supplier/ropehead", 
                          tags=["supplier ropehead 供应商:绳头装置"])
api_router.include_router(supplier_autorescue.router, 
                          prefix="/supplier/autorescue", 
                          tags=["supplier autorescue 供应商:自动救援装置"])
api_router.include_router(supplier_icard.router, 
                          prefix="/supplier/icard", 
                          tags=["supplier icard 供应商:IC卡"])
api_router.include_router(supplier_safebrake.router, 
                          prefix="/supplier/safebrake", 
                          tags=["supplier safebrake 供应商:安全钳"])