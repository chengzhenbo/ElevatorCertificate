from typing import Optional,List
from datetime import datetime,date
from uuid import UUID

from pydantic import BaseModel

from schemas.supplier import DataState

class WireRopeBase(BaseModel):
    wr_contract_no: Optional[str] = None
    wr_product_name: Optional[str] = None
    wr_dept_name: Optional[str] = None
    wr_product_testing_cert: Optional[str] = None
    wr_product_model: Optional[str] = None
    wr_product_matric: Optional[str] = None
    wr_product_value: Optional[float] = None
    wr_product_num: Optional[int] = None

class WireRopeCreate(WireRopeBase):
    user_id: Optional[int] = None
    data_state: Optional[str] = DataState.Submited
    create_time: Optional[datetime] = datetime.now()
    update_time: Optional[datetime] = datetime.now()
    
# Properties shared by models stored in DB
class WireRopeInDBBase(WireRopeBase):
    data_state: Optional[str] = None
    safety_machine_id: Optional[UUID] = None
    user_id: Optional[int] = None 
    create_time: Optional[datetime] = None
    
    class Config:
        orm_mode = True

# Properties to return to client
class WireRope(WireRopeInDBBase):
    pass

class ListWireRopes(BaseModel):
    wire_ropes: List[WireRopeInDBBase]
