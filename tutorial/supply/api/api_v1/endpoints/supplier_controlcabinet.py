from typing import List, Any
from uuid import UUID

from fastapi import APIRouter, Depends, UploadFile, status, HTTPException
from sqlalchemy.orm import Session
from io import BytesIO

from core.excel_reader import read_supplier_data, SupplierType
import crud.crud_supplier_controlcabinet as crud_supplier_controlcabinet
import schemas as schemas
from api import deps

router = APIRouter()

@router.get('/controlcabinets', response_model=List[schemas.ControlCabinet])
def read_controlcabinets(db: Session = Depends(deps.get_db),
                     skip: int = 0,
                     limit: int = 100)->Any:
    objs = crud_supplier_controlcabinet.get_control_cabinets(db=db, 
                                                          skip=skip, 
                                                          limit=limit)
    return objs


@router.post('/control_cabinets', 
             response_model = schemas.ListControlCabinets, 
             status_code=status.HTTP_201_CREATED)
async def upload_control_cabinets(file: UploadFile, 
                            db: Session = Depends(deps.get_db)):
    if file.filename.endswith('.xlsx'):
        f = await file.read()
        excelfile = BytesIO(f)
        control_cabinets_df = read_supplier_data(supplier_type=SupplierType.KONGZHIGUI, 
                                               path = excelfile)
        if control_cabinets_df.valid_dataframe.empty:
            raise HTTPException(status_code=400,
                                detail="控制柜装置的有效数据为空.")
        records = control_cabinets_df.valid_dataframe.to_dict('records')
        control_cabinets = []
        for record in records:
            control_cabinet = schemas.ControlCabinetCreate(**record)
            db_obj = crud_supplier_controlcabinet.create_control_cabinet(db=db,
                                                                     control_cabinet = control_cabinet)
            if not db_obj:
                raise HTTPException(status_code=404,
                                    detail="控制柜数据未能正常写入数据库.")
            control_cabinets.append(db_obj)
       
        return {"control_cabinets":control_cabinets}
    else:
        raise HTTPException(status_code=404, detail="File can not open")

@router.delete('/delete_control_cabinet/{control_cabinet_id}', 
               status_code=status.HTTP_204_NO_CONTENT)
def delete_control_cabinet_by_id(control_cabinet_id:UUID, db: Session = Depends(deps.get_db)):
    db_obj = crud_supplier_controlcabinet.delete_control_cabinet(db=db, 
                                                         control_cabinet_id = control_cabinet_id)
    if not db_obj:
        raise HTTPException(status_code=404,
                            detail="控制柜数据未能正常从数据库中删除.")

@router.delete('/delete_control_cabinets/{num_days}')
def delete_control_cabinet_by_numdays(db: Session = Depends(deps.get_db), num_days:int = 1):
    count = crud_supplier_controlcabinet.delete_control_cabinet_on_days(db=db, num_days = num_days)
    if count > 0:
        return {"num of objs deleted": count}
    else:
        raise HTTPException(status_code=404,
                            detail="没有删除数据.")