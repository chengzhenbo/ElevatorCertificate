from fastapi import APIRouter

from api.api_v1.endpoints import (supplier_board,
                                    supplier_ropehead,
                                    supplier_autorescue,
                                    supplier_icard,
                                    supplier_safebrake,
                                    supplier_speedlimiter,
                                    supplier_buffer,
                                    supplier_machine,
                                    supplier_wirerope,
                                    supplier_buffer_speedlimiter,
                                    supplier_doorsystem,
                                    supplier_controlcabinet)

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
api_router.include_router(supplier_speedlimiter.router, 
                          prefix="/supplier/speedlimiter", 
                          tags=["supplier speedlimiter 供应商:限速器"])
api_router.include_router(supplier_buffer_speedlimiter.router, 
                          prefix="/supplier/buffer_speedlimiter", 
                          tags=["supplier buffer_speedlimiter 供应商:安全钳与限速器"])
api_router.include_router(supplier_buffer.router, 
                          prefix="/supplier/buffer", 
                          tags=["supplier buffer 供应商:缓冲器"])
api_router.include_router(supplier_machine.router, 
                          prefix="/supplier/machine", 
                          tags=["supplier machine 供应商:主机"])
api_router.include_router(supplier_wirerope.router, 
                          prefix="/supplier/wirerope", 
                          tags=["supplier wirerope 供应商:钢丝绳"])
api_router.include_router(supplier_doorsystem.router, 
                          prefix="/supplier/doorsystem", 
                          tags=["supplier doorsystem 供应商:门系统"])
api_router.include_router(supplier_controlcabinet.router, 
                          prefix="/supplier/controlcabinet", 
                          tags=["supplier controlcabinet 供应商:控制柜"])