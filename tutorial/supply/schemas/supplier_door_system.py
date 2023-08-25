from typing import Optional,List
from datetime import datetime,date
from uuid import UUID

from pydantic import BaseModel

from schemas.supplier import DataState

class DoorSystemBase(BaseModel):
    contract_no: Optional[str] = None
    dept_name: Optional[str] = None
    type_name: Optional[str] = None
    model: Optional[str] = None
    batch_no: Optional[str] = None
    type_testing_cert_no: Optional[str] = None
    manufacture_date: Optional[date] = None
    remark: Optional[str] = None

class DoorSystemCreate(DoorSystemBase):
    user_id: Optional[int] = None
    data_state: Optional[str] = DataState.Submited
    create_time: Optional[datetime] = datetime.now()
    update_time: Optional[datetime] = datetime.now()
    
# Properties shared by models stored in DB
class DoorSystemInDBBase(DoorSystemBase):
    data_state: Optional[str] = None
    door_system_id: Optional[UUID] = None
    user_id: Optional[int] = None 
    create_time: Optional[datetime] = None
    

    class Config:
        orm_mode = True

# Properties to return to client
class DoorSystem(DoorSystemInDBBase):
    pass

class ListDoorSystems(BaseModel):
    door_systems: List[DoorSystemInDBBase]