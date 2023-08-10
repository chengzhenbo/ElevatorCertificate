from typing import List, Any
from uuid import UUID

from fastapi import APIRouter, Depends, UploadFile, status, HTTPException
from sqlalchemy.orm import Session
from io import BytesIO

from core.excel_reader import read_supplier_data, SupplierType
import crud.crud_supplier_safe_brake as crud_supplier_safe_brake
import schemas as schemas
from api import deps

router = APIRouter()

@router.get('/safe_brakes', response_model=List[schemas.SafeBrake])
def read_safe_brakes(db: Session = Depends(deps.get_db),
                     skip: int = 0,
                     limit: int = 100)->Any:
    objs = crud_supplier_safe_brake.get_safe_brake(db=db, skip=skip, limit=limit)
    return objs

@router.post('/safe_brakes', 
             response_model = schemas.ListSafeBrakes, 
             status_code=status.HTTP_201_CREATED)
async def upload_safe_brakes(file: UploadFile, 
                            db: Session = Depends(deps.get_db)):
    if file.filename.endswith('.xlsx'):
        f = await file.read()
        excelfile = BytesIO(f)
        safe_brakes_df = read_supplier_data(supplier_type=SupplierType.ANQUANQIAN, 
                                       path = excelfile)
        if safe_brakes_df.valid_dataframe.empty:
            raise HTTPException(
                    status_code=400,
                    detail="安全钳装置的有效数据为空.")
        safe_brakes = []
        for _, row in safe_brakes_df.valid_dataframe.iterrows():
            safe_brake_schema = schemas.SafeBrakeCreate(contract_no = row["HeTongHao"],
                                                user_name = row["YongHuMingCheng"],
                                                dept_name = row["ZhiZhaoDanWei"],
                                                product_type_name = row["SheBeiPingZhong"],
                                                product_model = row["XingHao"],
                                                product_speed = row["ShuDu"],
                                                product_no = row["BianHao"],
                                                product_testing_cert_no = row["ZhengShuBianHao"],
                                                manufacture_date = row["ZhiZhaoRiQi"],
                                                user_id = 1)
            safe_brake_model = crud_supplier_safe_brake.create_safe_brake(db=db,
                                                                          safe_brake = safe_brake_schema)
            safe_brakes.append(safe_brake_model)
        invalid_datanum:int = safe_brakes_df.invalid_dataframe.shape[0] 
        return {"safe_brakes":safe_brakes, 
                "invalid_data_num":invalid_datanum}
    else:
        raise HTTPException(status_code=404, detail="File can not open")

@router.delete('/delete_safe_brake/{safe_brake_id}', status_code=status.HTTP_204_NO_CONTENT)
def delete_safe_brake_by_id(safe_brake_id:UUID, db: Session = Depends(deps.get_db)):
    crud_supplier_safe_brake.delete_safe_brake(db=db, safe_brake_id = safe_brake_id)

@router.delete('/delete_safe_brakes/{num_days}', status_code=status.HTTP_204_NO_CONTENT)
def delete_safe_brake_by_numdays(db: Session = Depends(deps.get_db), num_days:int = 1):
    crud_supplier_safe_brake.delete_safe_brake_on_days(db=db, num_days = num_days)