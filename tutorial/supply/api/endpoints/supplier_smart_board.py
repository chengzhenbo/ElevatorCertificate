from fastapi import APIRouter, Depends, UploadFile, status, HTTPException
from sqlalchemy.orm import Session
from io import BytesIO

from core.excel_reader import read_supplier_data, SupplierType
from crud.crud_supplier import create_smart_board
import schemas as schemas
from api import deps

router = APIRouter()

@router.post('/smartboad', response_model = schemas.ListSmartBoards, status_code=status.HTTP_201_CREATED)
async def upload_smartboad(file: UploadFile, db: Session = Depends(deps.get_db)):
    if file.filename.endswith('.xlsx'):
        f = await file.read()
        excelfile = BytesIO(f)
        product_parts = read_supplier_data(supplier_type=SupplierType.ZHUBAN_SMART, 
                                           path = excelfile)
        smartboards = []
        for _, row in product_parts.iterrows():
            smartboad_create = schemas.SmartBoardCreate(contract_no = row["HeTongHao"],
                                                      dept_name = row["ZhiZaoDanWei"],
                                                      smartb_model = row["ChanPingXingHao"],
                                                      smartb_manufacture_batch_no = row["ZhiZaoBianHao"],
                                                      smartb_type_testing_cert_no = row["ZhengShuBianHao"],
                                                      smartb_manufacture_date = row["ZhiZaoRiQi"],
                                                      user_id = 1)
            db_smart_board = create_smart_board(db=db,
                                                smartboard = smartboad_create)
            smartboards.append(db_smart_board)
        return {"smartboards":smartboards}
    else:
        raise HTTPException(status_code=404, detail="File can not open")