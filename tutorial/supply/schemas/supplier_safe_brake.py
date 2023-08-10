from typing import Optional,List
from datetime import datetime,date
from uuid import UUID

from pydantic import BaseModel

class SafeBrakeBase(BaseModel):
    contract_no: Optional[str] = None
    user_name: Optional[str] = None
    dept_name: Optional[str] = None
    product_type_name: Optional[str] = None
    product_model: Optional[str] = None
    product_speed: Optional[float] = None
    product_no: Optional[str] = None
    product_testing_cert_no: Optional[str] = None
    manufacture_date: Optional[date] = None

class SafeBrakeCreate(SafeBrakeBase):
    user_id: Optional[int] = None
    
# Properties shared by models stored in DB
class SafeBrakeInDBBase(SafeBrakeBase):
    safe_brake_id: Optional[UUID] = None
    user_id: Optional[int] = None 
    create_time: Optional[datetime] = None

    class Config:
        orm_mode = True

# Properties to return to client
class SafeBrake(SafeBrakeInDBBase):
    pass

class ListSafeBrakes(BaseModel):
    safe_brakes: List[SafeBrakeInDBBase]
    invalid_data_num: int = 0