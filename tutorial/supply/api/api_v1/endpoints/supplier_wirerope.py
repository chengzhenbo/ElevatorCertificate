from typing import List, Any
from uuid import UUID

from fastapi import APIRouter, Depends, UploadFile, status, HTTPException
from sqlalchemy.orm import Session
from io import BytesIO

from core.excel_reader import read_supplier_data, SupplierType
import crud.crud_supplier_wire_rope as crud_supplier_wire_rope
import schemas as schemas
from api import deps

router = APIRouter()

@router.get('/wire_ropes', response_model=List[schemas.WireRope])
def read_wire_ropes(db: Session = Depends(deps.get_db),
                     skip: int = 0,
                     limit: int = 100)->Any:
    objs = crud_supplier_wire_rope.get_wire_ropes(db=db, skip=skip, limit=limit)
    return objs

@router.post('/wire_ropes', 
             response_model = schemas.ListWireRopes, 
             status_code=status.HTTP_201_CREATED)
async def upload_wire_ropes(file: UploadFile, 
                            db: Session = Depends(deps.get_db)):
    if file.filename.endswith('.xlsx'):
        f = await file.read()
        excelfile = BytesIO(f)
        wire_ropes_df = read_supplier_data(supplier_type=SupplierType.GANGSHISHENG, 
                                               path = excelfile)
        if wire_ropes_df.valid_dataframe.empty:
            raise HTTPException(status_code=400,
                                detail="钢丝绳装置的有效数据为空.")
        records = wire_ropes_df.valid_dataframe.to_dict('records')
        wire_ropes = []
        for record in records:
            wire_rope = schemas.WireRopeCreate(**record)
            db_obj = crud_supplier_wire_rope.create_wire_rope(db=db,
                                                                     wire_rope = wire_rope)
            if not db_obj:
                raise HTTPException(status_code=404,
                                    detail="钢丝绳数据未能正常写入数据库.")
            wire_ropes.append(db_obj)
       
        return {"wire_ropes":wire_ropes}
    else:
        raise HTTPException(status_code=404, detail="File can not open")

@router.delete('/delete_wire_rope/{wire_rope_id}', 
               status_code=status.HTTP_204_NO_CONTENT)
def delete_wire_rope_by_id(wire_rope_id:UUID, db: Session = Depends(deps.get_db)):
    db_obj = crud_supplier_wire_rope.delete_wire_rope(db=db, 
                                                    wire_rope_id = wire_rope_id)
    if not db_obj:
        raise HTTPException(status_code=404,
                            detail="钢丝绳数据未能正常从数据库中删除.")
    
@router.delete('/delete_wire_ropes/{num_days}')
def delete_wire_rope_by_numdays(db: Session = Depends(deps.get_db), num_days:int = 1):
    count = crud_supplier_wire_rope.delete_wire_rope_on_days(db=db, num_days = num_days)
    if count > 0:
        return {"num of objs deleted": count}
    else:
        raise HTTPException(status_code=404,
                            detail="没有删除数据.")
    