from typing import Optional,List
from datetime import datetime
from uuid import UUID

from pydantic import BaseModel

class IcCardBase(BaseModel):
    contract_no: Optional[str] = None
    icard_model: Optional[str] = None
    icard_no: Optional[str] = None

class IcCardCreate(IcCardBase):
    user_id: Optional[int] = None
    
# Properties shared by models stored in DB
class IcCardInDBBase(IcCardBase):
    icard_id: Optional[UUID] = None
    user_id: Optional[int] = None 
    create_time: Optional[datetime] = None

    class Config:
        orm_mode = True

# Properties to return to client
class IcCard(IcCardInDBBase):
    pass

class ListIcCards(BaseModel):
    icards: List[IcCardInDBBase]
    invalid_data_num: int = 0