from typing import Optional,List
from datetime import date,datetime
from uuid import UUID

from pydantic import BaseModel

class RopeHeadBase(BaseModel):
    contract_no: Optional[str] = None
    dept_name: Optional[str] = None
    ropehc_name: Optional[str] = None
    ropehc_model: Optional[str] = None
    ropehc_manufacture_batch_no: Optional[str] = None
    ropehc_type_testing_cert_no: Optional[str] = None
    ropehc_manufacture_date: Optional[date] = None
    
class RopeHeadCreate(RopeHeadBase):
    user_id: Optional[int] = None
    
# Properties shared by models stored in DB
class RopeHeadInDBBase(RopeHeadBase):
    rope_head_id: Optional[UUID] = None
    user_id: Optional[int] = None 
    create_time: Optional[datetime] = None

    class Config:
        orm_mode = True

# Properties to return to client
class RopeHead(RopeHeadInDBBase):
    pass

class ListRopeHeads(BaseModel):
    ropeheads: List[RopeHeadInDBBase]
    invalid_data_num: int = 0