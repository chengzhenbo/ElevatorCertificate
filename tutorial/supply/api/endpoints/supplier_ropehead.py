from typing import List, Any
from uuid import UUID

from fastapi import APIRouter, Depends, UploadFile, status, HTTPException
from sqlalchemy.orm import Session
from io import BytesIO

from core.excel_reader import read_supplier_data, SupplierType
import crud.crud_supplier_ropehead as crud_supplier_ropehead
import schemas as schemas
from api import deps

router = APIRouter()

@router.get('/rope_heads', response_model=List[schemas.RopeHead])
def read_rope_heads(db: Session = Depends(deps.get_db),
                      skip: int = 0,
                      limit: int = 100)->Any:
    rope_heads = crud_supplier_ropehead.get_rope_head(db=db, skip=skip, limit=limit)
    return rope_heads

@router.post('/rope_heads', 
             response_model = schemas.ListRopeHeads, 
             status_code=status.HTTP_201_CREATED)
async def upload_rope_heads(file: UploadFile, 
                            db: Session = Depends(deps.get_db)):
    if file.filename.endswith('.xlsx'):
        f = await file.read()
        excelfile = BytesIO(f)
        rope_head = read_supplier_data(supplier_type=SupplierType.SHENGTOUZHUHE, 
                                       path = excelfile)

        if rope_head.valid_dataframe.empty:
            raise HTTPException(
                    status_code=400,
                    detail="绳头组合的有效数据为空.")

        ropeheads = []
        for _, row in rope_head.valid_dataframe.iterrows():
            db_rope_head = crud_supplier_ropehead.create_rope_head(db=db,
                                              ropehead = schemas.RopeHeadCreate(contract_no = row["HeTongHao"],
                                                            dept_name = row["ZhiZhaoDanWei"],
                                                            ropehc_name = row["SheBeiPingZhong"],
                                                            ropehc_model = row["XingHao"],
                                                            ropehc_manufacture_batch_no = row["PiChiHao"],
                                                            ropehc_type_testing_cert_no = row["ZhenShuBianHao"],
                                                            ropehc_manufacture_date = row["ZhiZhaoRiQi"],
                                                            user_id = 1))
            ropeheads.append(db_rope_head)
        invalid_datanum:int = rope_head.invalid_dataframe.shape[0] 
        return {"ropeheads":ropeheads, 
                "invalid_data_num":invalid_datanum}
    else:
        raise HTTPException(status_code=404, detail="File can not open")
    
@router.delete('/delete_ropeheads/{num_days}', status_code=status.HTTP_204_NO_CONTENT)
def delete_ropehead_by_numdays(db: Session = Depends(deps.get_db), num_days:int = 1):
    crud_supplier_ropehead.delete_rope_head_on_days(db=db, num_days = num_days)

@router.delete('/delete_ropehead/{rope_head_id}', status_code=status.HTTP_204_NO_CONTENT)
def delete_smartboard_by_id(rope_head_id:UUID, db: Session = Depends(deps.get_db)):
    crud_supplier_ropehead.delete_rope_head(db=db, rope_head_id = rope_head_id)