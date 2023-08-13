from typing import List, Any
from uuid import UUID

from fastapi import APIRouter, Depends, UploadFile, status, HTTPException
from sqlalchemy.orm import Session
from io import BytesIO

from core.excel_reader import read_supplier_data, SupplierType
import crud.crud_supplier_autorescue as crud_supplier_autorescue
import schemas as schemas
from api import deps

router = APIRouter()

@router.get('/auto_rescues', response_model=List[schemas.AutoRescue])
def read_auto_rescues(db: Session = Depends(deps.get_db),
                      skip: int = 0,
                      limit: int = 100)->Any:
    objs = crud_supplier_autorescue.get_auto_rescue(db=db, skip=skip, limit=limit)
    return objs

@router.post('/auto_rescues', 
             response_model = schemas.ListAutoRescues, 
             status_code=status.HTTP_201_CREATED)
async def upload_auto_rescues(file: UploadFile, 
                            db: Session = Depends(deps.get_db)):
    if file.filename.endswith('.xlsx'):
        f = await file.read()
        excelfile = BytesIO(f)
        auto_rescues_df = read_supplier_data(supplier_type=SupplierType.ZHIDONGJIUYUAN, 
                                       path = excelfile)
        if auto_rescues_df.valid_dataframe.empty:
            raise HTTPException(
                    status_code=400,
                    detail="救援装置的有效数据为空.")
        auto_rescues = []
        for _, row in auto_rescues_df.valid_dataframe.iterrows():
            autorescue = schemas.AutoRescueCreate(contract_no = row["HeTongHao"],
                                                  auto_rescue_model = row["XingHao"],
                                                  auto_rescue_no = row["BianHao"],
                                                  user_id = 1)
            auto_rescue = crud_supplier_autorescue.create_auto_rescue(db=db,
                                                                      autorescue = autorescue)
            auto_rescues.append(auto_rescue)
        invalid_datanum:int = auto_rescues_df.invalid_dataframe.shape[0] 
        return {"auto_rescues":auto_rescues, 
                "invalid_data_num":invalid_datanum}
    else:
        raise HTTPException(status_code=404, detail="File can not open")

@router.delete('/delete_auto_rescue/{auto_rescue_id}', status_code=status.HTTP_204_NO_CONTENT)
def delete_autorescue_by_id(auto_rescue_id:UUID, db: Session = Depends(deps.get_db)):
    crud_supplier_autorescue.delete_auto_rescue(db=db, auto_rescue_id = auto_rescue_id)

@router.delete('/delete_autorescues/{num_days}', status_code=status.HTTP_204_NO_CONTENT)
def delete_autorescue_by_numdays(db: Session = Depends(deps.get_db), num_days:int = 1):
    crud_supplier_autorescue.delete_auto_rescue_on_days(db=db, num_days = num_days)