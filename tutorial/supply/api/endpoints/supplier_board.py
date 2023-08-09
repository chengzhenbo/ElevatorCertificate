from typing import List, Any
from uuid import UUID

from fastapi import APIRouter, Depends, UploadFile, status, HTTPException
from sqlalchemy.orm import Session
from io import BytesIO

from core.excel_reader import read_supplier_data, SupplierType
import crud.crud_supplier_board as crud_supplier_board
import schemas as schemas
from api import deps

router = APIRouter()

@router.get('/smart_boards', response_model=List[schemas.SmartBoard])
def read_smart_boards(db: Session = Depends(deps.get_db),
                      skip: int = 0,
                      limit: int = 100)->Any:
    smart_boards = crud_supplier_board.get_smart_boards(db=db, skip=skip, limit=limit)
    return smart_boards

@router.get('/lvct_boards', response_model=List[schemas.LvctBoard])
def read_lvct_boards(db: Session = Depends(deps.get_db),
                      skip: int = 0,
                      limit: int = 100)->Any:
    lvct_boards = crud_supplier_board.get_lvct_boards(db=db, skip=skip, limit=limit)
    return lvct_boards

@router.post('/smart_lvct_boards', 
             response_model = schemas.ListBoards, 
             status_code=status.HTTP_201_CREATED)
async def upload_boards(file: UploadFile, 
                       db: Session = Depends(deps.get_db)):
    if file.filename.endswith('.xlsx'):
        f = await file.read()
        excelfile = BytesIO(f)
        
        lvctboard = read_supplier_data(supplier_type=SupplierType.ZHUBAN_LVCT, 
                                           path = excelfile)
        smartboard = read_supplier_data(supplier_type=SupplierType.ZHUBAN_SMART, 
                                           path = excelfile)
        if lvctboard.valid_dataframe.empty:
            raise HTTPException(
                    status_code=400,
                    detail="lvct 主板有效数据为空.")
        if smartboard.valid_dataframe.empty:
            raise HTTPException(
                    status_code=400,
                    detail="smart 主板有效数据为空.")
        smartboards = []
        lvctboards = []
        for _, row in smartboard.valid_dataframe.iterrows():
            db_smart_board = crud_supplier_board.create_smart_board(db=db,
                                                smartboard = schemas.SmartBoardCreate(contract_no = row["HeTongHao"],
                                                      dept_name = row["ZhiZaoDanWei"],
                                                      smartb_model = row["ChanPingXingHao"],
                                                      smartb_manufacture_batch_no = row["ZhiZaoBianHao"],
                                                      smartb_type_testing_cert_no = row["ZhengShuBianHao"],
                                                      smartb_manufacture_date = row["ZhiZhaoRiQi"],
                                                      user_id = 1))
            smartboards.append(db_smart_board)
        for _, row in lvctboard.valid_dataframe.iterrows():
            db_lvct_board = crud_supplier_board.create_lvct_board(db=db,
                                              lvctboard = schemas.LvctBoardCreate(contract_no = row["HeTongHao"],
                                                      dept_name = row["ZhiZaoDanWei"],
                                                      lvct_model = row["ChanPingXingHao"],
                                                      lvct_manufacture_batch_no = row["ZhiZaoBianHao"],
                                                      lvct_type_testing_cert_no = row["ZhengShuBianHao"],
                                                      lvct_manufacture_date = row["ZhiZhaoRiQi"],
                                                      user_id = 1))
            lvctboards.append(db_lvct_board)
        invalid_datanum:int = lvctboard.invalid_dataframe.shape[0] + smartboard.invalid_dataframe.shape[0] 
        return {"smartboards":smartboards, 
                "lvctboards":lvctboards,
                "invalid_data_num":invalid_datanum}
    else:
        raise HTTPException(status_code=404, detail="File can not open")

@router.delete('/delete_smartboards/{num_days}', status_code=status.HTTP_204_NO_CONTENT)
def delete_smartboard_by_numdays(db: Session = Depends(deps.get_db), num_days:int = 1):
    crud_supplier_board.delete_smart_board_on_days(db=db, num_days = num_days)

@router.delete('/delete_lvctboards/{num_days}', status_code=status.HTTP_204_NO_CONTENT)
def delete_lvctboard_by_numdays(db: Session = Depends(deps.get_db), num_days:int = 1):
    crud_supplier_board.delete_lvct_board_on_days(db=db, num_days = num_days)

@router.delete('/delete_smartboard/{smart_board_id}', status_code=status.HTTP_204_NO_CONTENT)
def delete_smartboard_by_id(smart_board_id:UUID, db: Session = Depends(deps.get_db)):
    crud_supplier_board.delete_smart_board(db=db, smart_board_id = smart_board_id)

@router.delete('/delete_lvctboard/{lvct_board_id}', status_code=status.HTTP_204_NO_CONTENT)
def delete_lvctboard_by_id(lvct_board_id:UUID, db: Session = Depends(deps.get_db)):
    crud_supplier_board.delete_lvct_board(db=db, lvct_board_id = lvct_board_id)