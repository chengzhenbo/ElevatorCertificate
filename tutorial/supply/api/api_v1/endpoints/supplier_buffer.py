from typing import List, Any
from uuid import UUID

from fastapi import APIRouter, Depends, UploadFile, status, HTTPException
from sqlalchemy.orm import Session
from io import BytesIO

from core.excel_reader import read_supplier_data, SupplierType
import crud.crud_supplier_buffer as crud_supplier_buffer
import schemas as schemas
from api import deps

router = APIRouter()

@router.get('/buffers', response_model=List[schemas.Buffer])
def read_buffers(db: Session = Depends(deps.get_db),
                     skip: int = 0,
                     limit: int = 100)->Any:
    objs = crud_supplier_buffer.get_buffers(db=db, skip=skip, limit=limit)
    return objs

@router.post('/buffers', 
             response_model = schemas.ListBuffers, 
             status_code=status.HTTP_201_CREATED)
async def upload_buffers(file: UploadFile, 
                            db: Session = Depends(deps.get_db)):
    if file.filename.endswith('.xlsx'):
        f = await file.read()
        excelfile = BytesIO(f)
        buffers_df = read_supplier_data(supplier_type=SupplierType.HUANCHONGQI, 
                                               path = excelfile)
        if buffers_df.valid_dataframe.empty:
            raise HTTPException(status_code=400,
                                detail="缓冲器装置的有效数据为空.")
        records = buffers_df.valid_dataframe.to_dict('records')
        buffers = []
        for record in records:
            buffer = schemas.BufferCreate(**record)
            
            db_obj = crud_supplier_buffer.create_buffer(db=db,
                                                        buffer = buffer)
            if not db_obj:
                raise HTTPException(status_code=404,
                                    detail="缓冲器数据未能正常写入数据库.")
            buffers.append(db_obj)
       
        return {"buffers":buffers, 
                "invalid_data_num":buffers_df.invalid_dataframe.shape[0]}
    else:
        raise HTTPException(status_code=404, detail="File can not open")

@router.delete('/delete_buffer/{buffer_id}', 
               status_code=status.HTTP_204_NO_CONTENT)
def delete_buffer_by_id(buffer_id:UUID, db: Session = Depends(deps.get_db)):
    db_obj = crud_supplier_buffer.delete_buffer(db=db, 
                                                    buffer_id = buffer_id)
    if not db_obj:
        raise HTTPException(status_code=404,
                            detail="缓冲器数据未能正常从数据库中删除.")
    
@router.delete('/delete_buffers/{num_days}')
def delete_buffer_by_numdays(db: Session = Depends(deps.get_db), num_days:int = 1):
    count = crud_supplier_buffer.delete_buffer_on_days(db=db, num_days = num_days)
    if count > 0:
        return {"num of objs deleted": count}
    else:
        raise HTTPException(status_code=404,
                            detail="没有删除数据.")