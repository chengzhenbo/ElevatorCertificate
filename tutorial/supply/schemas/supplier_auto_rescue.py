from typing import Optional,List
from datetime import datetime
from uuid import UUID

from pydantic import BaseModel

class AutoRescueBase(BaseModel):
    contract_no: Optional[str] = None
    # dept_name: Optional[str] = None
    auto_rescue_model: Optional[str] = None
    auto_rescue_no: Optional[str] = None

class AutoRescueCreate(AutoRescueBase):
    user_id: Optional[int] = None
    
# Properties shared by models stored in DB
class AutoRescueInDBBase(AutoRescueBase):
    auto_rescue_id: Optional[UUID] = None
    user_id: Optional[int] = None 
    create_time: Optional[datetime] = None

    class Config:
        orm_mode = True

# Properties to return to client
class AutoRescue(AutoRescueInDBBase):
    pass

class ListAutoRescues(BaseModel):
    auto_rescues: List[AutoRescueInDBBase]
    invalid_data_num: int = 0