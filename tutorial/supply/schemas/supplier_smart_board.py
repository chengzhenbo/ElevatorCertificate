from typing import Optional,List
from datetime import datetime

from pydantic import BaseModel


class SmartBoardBaseSchema(BaseModel):
    contract_no : Optional[str] = None
    dept_id : Optional[int] = None
    smartb_model : Optional[str] = None
    smartb_manufacture_batch_no : Optional[str] = None
    smartb_type_testing_cert_no : Optional[str] = None
    smartb_manufacture_date : Optional[datetime] = None
    user_id : Optional[int] = None

class SmartBoardCreateSchema(SmartBoardBaseSchema):
    pass

# Properties to return to client
class SmartBoardSchema(SmartBoardBaseSchema):
    pass

class ListSmartBoardSchema(BaseModel):
    smartboards: List[SmartBoardBaseSchema]