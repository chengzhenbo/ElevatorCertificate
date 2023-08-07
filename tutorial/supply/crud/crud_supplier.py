from sqlalchemy.orm import Session

from models.supplier import SupplierSmartBoard
from schemas.supplier_smart_board import SmartBoardCreate

def create_smart_board(db: Session, 
                       smartboard: SmartBoardCreate)->SupplierSmartBoard:
    db_smartboard = SupplierSmartBoard(contract_no = smartboard.contract_no,
                                            dept_name = smartboard.dept_name,
                                            smartb_model = smartboard.smartb_model,
                                            smartb_manufacture_batch_no = smartboard.smartb_manufacture_batch_no,
                                            smartb_type_testing_cert_no = smartboard.smartb_type_testing_cert_no,
                                            smartb_manufacture_date = smartboard.smartb_manufacture_date,
                                            user_id = smartboard.user_id)
    db.add(db_smartboard)
    db.commit()
    db.refresh(db_smartboard)
    return db_smartboard