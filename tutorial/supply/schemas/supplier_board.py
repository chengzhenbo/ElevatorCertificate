from typing import Optional,List
from datetime import date
from uuid import UUID

from pydantic import BaseModel


class SmartBoardBase(BaseModel):
    contract_no: Optional[str] = None
    dept_name: Optional[str] = None
    smartb_model: Optional[str] = None
    smartb_manufacture_batch_no: Optional[str] = None
    smartb_type_testing_cert_no: Optional[str] = None
    smartb_manufacture_date: Optional[date] = None
    
class SmartBoardCreate(SmartBoardBase):
    user_id: Optional[int] = None
    

# Properties shared by models stored in DB
class SmartBoardInDBBase(SmartBoardBase):
    smartb_id: Optional[UUID] = None
    user_id: Optional[int] = None 

    class Config:
        orm_mode = True

class ListSmartBoards(BaseModel):
    smartboards: List[SmartBoardInDBBase]

# Properties to return to client
class SmartBoard(SmartBoardInDBBase):
    pass

class LvctBoardBase(BaseModel):
    contract_no: Optional[str] = None
    dept_name: Optional[str] = None
    lvct_model: Optional[str] = None
    lvct_manufacture_batch_no: Optional[str] = None
    lvct_type_testing_cert_no: Optional[str] = None
    lvct_manufacture_date: Optional[date] = None
    
class LvctBoardCreate(LvctBoardBase):
    user_id: Optional[int] = None
    

# Properties shared by models stored in DB
class LvctBoardInDBBase(LvctBoardBase):
    lvctb_id: Optional[UUID] = None
    user_id: Optional[int] = None 

    class Config:
        orm_mode = True

class ListLvctBoards(BaseModel):
    lvctboards: List[LvctBoardInDBBase]

# Properties to return to client
class LvctBoard(LvctBoardInDBBase):
    pass

class ListBoards(BaseModel):
    smartboards: List[SmartBoardInDBBase]
    lvctboards: List[LvctBoardInDBBase]

