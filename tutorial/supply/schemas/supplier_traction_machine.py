from typing import Optional,List
from datetime import datetime,date
from uuid import UUID

from pydantic import BaseModel

from schemas.supplier import DataState
from schemas.supplier_safety_machine import SafetyMachineInDBBase
from schemas.supplier_brake_machine import BrakeMachineInDBBase

class TractionMachineBase(BaseModel):
    contract_no: Optional[str] = None
    dept_name: Optional[str] = None
    product_type_name: Optional[str] = None
    product_model: Optional[str] = None
    product_no: Optional[str] = None
    product_testing_cert_no: Optional[str] = None
    manufacture_date: Optional[date] = None

class TractionMachineCreate(TractionMachineBase):
    user_id: Optional[int] = None
    data_state: Optional[str] = DataState.Submited
    create_time: Optional[datetime] = datetime.now()
    update_time: Optional[datetime] = datetime.now()
    
# Properties shared by models stored in DB
class TractionMachineInDBBase(TractionMachineBase):
    data_state: Optional[str] = None
    traction_machine_id: Optional[UUID] = None
    user_id: Optional[int] = None 
    create_time: Optional[datetime] = None
    

    class Config:
        orm_mode = True

# Properties to return to client
class TractionMachine(TractionMachineInDBBase):
    pass

class ListTractionMachines(BaseModel):
    traction_machines: List[TractionMachineInDBBase]

class SupplierMachines(BaseModel):
    traction_machines: List[TractionMachineInDBBase]
    brake_machines: List[BrakeMachineInDBBase]
    safety_machines: List[SafetyMachineInDBBase]

