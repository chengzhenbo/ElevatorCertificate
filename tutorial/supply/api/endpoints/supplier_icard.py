from typing import List, Any
from uuid import UUID

from fastapi import APIRouter, Depends, UploadFile, status, HTTPException
from sqlalchemy.orm import Session
from io import BytesIO

from core.excel_reader import read_supplier_data, SupplierType
import crud.crud_supplier_icard as crud_supplier_icard
import schemas as schemas
from api import deps

router = APIRouter()

@router.get('/ic_cards', response_model=List[schemas.IcCard])
def read_ic_cards(db: Session = Depends(deps.get_db),
                      skip: int = 0,
                      limit: int = 100)->Any:
    objs = crud_supplier_icard.get_ic_card(db=db, skip=skip, limit=limit)
    return objs

@router.post('/ic_cards', 
             response_model = schemas.ListIcCards, 
             status_code=status.HTTP_201_CREATED)
async def upload_ic_cards(file: UploadFile, 
                          db: Session = Depends(deps.get_db)):
    if file.filename.endswith('.xlsx'):
        f = await file.read()
        excelfile = BytesIO(f)
        ic_cards_df = read_supplier_data(supplier_type=SupplierType.IC_CARD, 
                                         path = excelfile)
        if ic_cards_df.valid_dataframe.empty:
            raise HTTPException(status_code=400,
                                detail="ic卡装置的有效数据为空.")
        icards = []
        for _, row in ic_cards_df.valid_dataframe.iterrows():
            icard = schemas.IcCardCreate(contract_no = row["HeTongHao"],
                                        icard_model = row["XingHao"],
                                        icard_no = row["BianHao"],
                                        user_id = 1)
            obj_icard = crud_supplier_icard.create_ic_card(db=db,
                                                             icard = icard)
            icards.append(obj_icard)
        invalid_datanum:int = ic_cards_df.invalid_dataframe.shape[0] 
        return {"icards":icards, 
                "invalid_data_num":invalid_datanum}
    else:
        raise HTTPException(status_code=404, detail="File can not open")

@router.delete('/delete_ic_card/{icard_id}', status_code=status.HTTP_204_NO_CONTENT)
def delete_icard_by_id(icard_id:UUID, db: Session = Depends(deps.get_db)):
    crud_supplier_icard.delete_ic_card(db=db, icard_id = icard_id)

@router.delete('/delete_icards/{num_days}', status_code=status.HTTP_204_NO_CONTENT)
def delete_icard_by_numdays(db: Session = Depends(deps.get_db), num_days:int = 1):
    crud_supplier_icard.delete_ic_card_on_days(db=db, num_days = num_days)