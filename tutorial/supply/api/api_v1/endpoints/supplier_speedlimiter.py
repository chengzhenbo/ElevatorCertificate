from typing import List, Any
from uuid import UUID

from fastapi import APIRouter, Depends, UploadFile, status, HTTPException
from sqlalchemy.orm import Session
from io import BytesIO

from core.excel_reader import read_supplier_data, SupplierType
import crud.crud_supplier_speedlimiter as crud_supplier_speedlimiter
import schemas as schemas
from api import deps

router = APIRouter()

@router.get('/speed_limiters', response_model=List[schemas.SpeedLimiter])
def read_speed_limiters(db: Session = Depends(deps.get_db),
                     skip: int = 0,
                     limit: int = 100)->Any:
    objs = crud_supplier_speedlimiter.get_speed_limiters(db=db, skip=skip, limit=limit)
    return objs

@router.post('/speed_limiters', 
             response_model = schemas.ListSpeedLimiters, 
             status_code=status.HTTP_201_CREATED)
async def upload_speed_limiters(file: UploadFile, 
                            db: Session = Depends(deps.get_db)):
    if file.filename.endswith('.xlsx'):
        f = await file.read()
        excelfile = BytesIO(f)
        speed_limiters_df = read_supplier_data(supplier_type=SupplierType.XIANSUQI, 
                                               path = excelfile)
        if speed_limiters_df.valid_dataframe.empty:
            raise HTTPException(status_code=400,
                                detail="限速器装置的有效数据为空.")
        records = speed_limiters_df.valid_dataframe.to_dict('records')
        speed_limiters = []
        for record in records:
            speed_limiter = schemas.SpeedLimiterCreate(**record)
            db_obj = crud_supplier_speedlimiter.create_speed_limiter(db=db,
                                                                     speed_limiter = speed_limiter)
            if not db_obj:
                raise HTTPException(status_code=404,
                                    detail="限速器数据未能正常写入数据库.")
            speed_limiters.append(db_obj)
       
        return {"speed_limiters":speed_limiters, 
                "invalid_data_num":speed_limiters_df.invalid_dataframe.shape[0]}
    else:
        raise HTTPException(status_code=404, detail="File can not open")

@router.delete('/delete_speed_limiter/{speed_limiter_id}', 
               status_code=status.HTTP_204_NO_CONTENT)
def delete_speed_limiter_by_id(speed_limiter_id:UUID, db: Session = Depends(deps.get_db)):
    db_obj = crud_supplier_speedlimiter.delete_speed_limiter(db=db, 
                                                    speed_limiter_id = speed_limiter_id)
    if not db_obj:
        raise HTTPException(status_code=404,
                            detail="限速器数据未能正常从数据库中删除.")
    
@router.delete('/delete_speed_limiters/{num_days}')
def delete_speed_limiter_by_numdays(db: Session = Depends(deps.get_db), num_days:int = 1):
    count = crud_supplier_speedlimiter.delete_speed_limiter_on_days(db=db, num_days = num_days)
    if count > 0:
        return {"num of objs deleted": count}
    else:
        raise HTTPException(status_code=404,
                            detail="没有删除数据.")
    