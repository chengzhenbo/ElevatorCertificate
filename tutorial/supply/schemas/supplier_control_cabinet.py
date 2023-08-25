from typing import Optional,List
from datetime import datetime,date
from uuid import UUID

from pydantic import BaseModel

from schemas.supplier import DataState

class ControlCabinetBase(BaseModel):
    contract_no: Optional[str] = None
    dept_name: Optional[str] = None
    type_name: Optional[str] = None
    model: Optional[str] = None
    batch_no: Optional[str] = None
    type_testing_cert_no: Optional[str] = None
    manufacture_date: Optional[date] = None

class ControlCabinetCreate(ControlCabinetBase):
    user_id: Optional[int] = None
    data_state: Optional[str] = DataState.Submited
    create_time: Optional[datetime] = datetime.now()
    update_time: Optional[datetime] = datetime.now()
    
# Properties shared by models stored in DB
class ControlCabinetInDBBase(ControlCabinetBase):
    data_state: Optional[str] = None
    control_cabinet_id: Optional[UUID] = None
    user_id: Optional[int] = None 
    create_time: Optional[datetime] = None
    

    class Config:
        orm_mode = True

# Properties to return to client
class ControlCabinet(ControlCabinetInDBBase):
    pass

class ListControlCabinets(BaseModel):
    control_cabinets: List[ControlCabinetInDBBase]