from typing import Optional,List
from datetime import datetime,date
from uuid import UUID

from pydantic import BaseModel

from schemas.supplier import DataState

class BufferBase(BaseModel):
    contract_no: Optional[str] = None
    project_name: Optional[str] = None
    dept_name: Optional[str] = None
    product_type_name: Optional[str] = None
    product_model: Optional[str] = None
    product_speed: Optional[str] = None
    product_no: Optional[str] = None
    product_batch_no: Optional[str] = None
    product_testing_cert_no: Optional[str] = None
    manufacture_date: Optional[date] = None

class BufferCreate(BufferBase):
    user_id: Optional[int] = None
    data_state: Optional[str] = DataState.Submited
    create_time: Optional[datetime] = datetime.now()
    update_time: Optional[datetime] = datetime.now()
    
# Properties shared by models stored in DB
class BufferInDBBase(BufferBase):
    data_state: Optional[str] = None
    speed_limiter_id: Optional[UUID] = None
    user_id: Optional[int] = None 
    create_time: Optional[datetime] = None
    

    class Config:
        orm_mode = True

# Properties to return to client
class Buffer(BufferInDBBase):
    pass

class ListBuffers(BaseModel):
    buffers: List[BufferInDBBase]
    invalid_data_num: int = 0