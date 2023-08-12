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
            raise HTTPException(
                    status_code=400,
                    detail="限速器装置的有效数据为空.")
        records = speed_limiters_df.valid_dataframe.to_dict('records')
        
        safe_brakes:list[schemas.SpeedLimiterCreate] = [schemas.SpeedLimiterCreate(**r) for r in records]

        db_objects = crud_supplier_speedlimiter.create_speed_limiters(db=db,
                                                                      safe_brakes = safe_brakes)
        return {"speed_limiters":db_objects, 
                "invalid_data_num":speed_limiters_df.invalid_dataframe.shape[0]}
    else:
        raise HTTPException(status_code=404, detail="File can not open")