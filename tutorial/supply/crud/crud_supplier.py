from sqlalchemy.orm import Session

from models.supplier import SupplierSmartBoardModel
from schemas.supplier_smart_board import SmartBoardCreateSchema

def create_smart_board(db: Session, smartboard: SmartBoardCreateSchema):
    db_smartboard = SupplierSmartBoardModel(contract_no = smartboard.contract_no,
                                       dept_id = smartboard.dept_id,
                                       smartb_model = smartboard.smartb_model,
                                       smartb_manufacture_batch_no = smartboard.smartb_manufacture_batch_no,
                                       smartb_type_testing_cert_no = smartboard.smartb_type_testing_cert_no,
                                       smartb_manufacture_date= smartboard.smartb_manufacture_date)
    db.add(db_smartboard)
    db.commit()
    db.refresh(db_smartboard)
    return db_smartboard