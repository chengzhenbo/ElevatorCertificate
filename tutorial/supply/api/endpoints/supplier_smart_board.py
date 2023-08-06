from fastapi import APIRouter, Depends, UploadFile, status, HTTPException
from sqlalchemy.orm import Session
from io import BytesIO

from core.excel_reader import read_supplier_data, SupplierType
from crud.crud_supplier import create_smart_board
from schemas.smart_board import SmartBoardCreateSchema,ListSmartBoardSchema
from api import deps

router = APIRouter()

@router.get('/')
def index():
    return {"message":"hello"}

@router.post('/', response_model = ListSmartBoardSchema, status_code=status.HTTP_201_CREATED)
async def create(file: UploadFile, db: Session = Depends(deps.get_db)):
    if file.filename.endswith('.xlsx'):
        # Read it, 'f' type is bytes
        f = await file.read()
        excelfile = BytesIO(f)
        product_parts = read_supplier_data(supplier_type=SupplierType.ZHUBAN_SMART, 
                                           path = excelfile)
        smartboards:ListSmartBoardSchema = []
        for _, row in product_parts.iterrows():
            smartboad_create = SmartBoardCreateSchema(contract_no = row["HeTongHao"],
                                                        dept_id = 12,
                                                        smartb_model = row["ChanPingXingHao"],
                                                        smartb_manufacture_batch_no = row["ZhiZaoBianHao"],
                                                        smartb_type_testing_cert_no = row["ZhengShuBianHao"],
                                                        smartb_manufacture_date = row["ZhiZaoRiQi"])
            smartboards.append(smartboad_create)
            db_smart_board = create_smart_board(db=db,
                                             smartboard = smartboad_create)
        return {"smartboards":smartboards}
    else:
        raise HTTPException(status_code=404, detail="File can not open")