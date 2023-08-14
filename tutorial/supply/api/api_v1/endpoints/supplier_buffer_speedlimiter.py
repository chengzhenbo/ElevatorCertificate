from typing import List, Any
from uuid import UUID

from fastapi import APIRouter, Depends, UploadFile, status, HTTPException
from sqlalchemy.orm import Session
from io import BytesIO

from core.excel_reader import read_supplier_data, SupplierType
import crud as crud
import schemas as schemas
from api import deps

router = APIRouter()


@router.post('/buffer_speedlimiters', 
             response_model = schemas.Buffer_Speedlimiters, 
             status_code=status.HTTP_201_CREATED)
async def upload_buffer_speedlimiter(file: UploadFile, 
                                     db: Session = Depends(deps.get_db)):
    if file.filename.endswith('.xlsx'):
        f = await file.read()
        excelfile = BytesIO(f)
        buffers_df = read_supplier_data(supplier_type=SupplierType.HUANCHONGQI, 
                                               path = excelfile)
        speedlimiters_df = read_supplier_data(supplier_type=SupplierType.XIANSUQI, 
                                               path = excelfile)

        if buffers_df.valid_dataframe.empty:
            raise HTTPException(status_code=400,
                                detail="限速器装置有效数据为空.")
        if speedlimiters_df.valid_dataframe.empty:
            raise HTTPException(status_code=400,
                                detail="缓冲器装置有效数据为空.")

        buffer_records = buffers_df.valid_dataframe.to_dict('records')
        speedlimiter_records = speedlimiters_df.valid_dataframe.to_dict('records')

        buffers,speed_limiters = [],[]
        for record in buffer_records:
            buffer = schemas.BufferCreate(**record)
            db_obj = crud.crud_supplier_buffer.create_buffer(db=db,
                                                             buffer = buffer)
            if not db_obj:
                raise HTTPException(status_code=404,
                                    detail="缓冲器数据未能正常写入数据库.")
            buffers.append(db_obj)
        for record in speedlimiter_records:
            speed_limiter = schemas.SpeedLimiterCreate(**record)
            db_obj = crud.crud_supplier_speedlimiter.create_speed_limiter(db=db,
                                                        speed_limiter = speed_limiter)
            if not db_obj:
                raise HTTPException(status_code=404,
                                    detail="限速器数据未能正常写入数据库.")
            speed_limiters.append(db_obj)

        return {"buffers":buffers, 
                "speed_limiters":speed_limiters}
    else:
        raise HTTPException(status_code=404, detail="File can not open")

@router.delete('/delete_buffer_speedlimiters/{num_days}')
def delete_buffer_speedlimiter_by_numdays(db: Session = Depends(deps.get_db), num_days:int = 1):
    count_buffer, count_speedlimiter = 0, 0
    count_buffer = crud.crud_supplier_buffer.delete_buffer_on_days(db=db, num_days = num_days)
    count_speedlimiter = crud.crud_supplier_speedlimiter.delete_speed_limiter_on_days(db=db, num_days = num_days)
    
    return {"num of buffers deleted": count_buffer,
            "num of speedlimiters deleted": count_speedlimiter}