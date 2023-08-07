from sqlalchemy.orm import Session

from models.supplier import SupplierSmartBoard, SupplierLvctBoard
import schemas as schemas


def create_smart_board(db: Session, 
                       smartboard: schemas.SmartBoardCreate)->SupplierSmartBoard:
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

def create_lvct_board(db: Session, 
                      lvctboard: schemas.LvctBoardCreate)->SupplierLvctBoard:
    db_lvctboard = SupplierLvctBoard(contract_no = lvctboard.contract_no,
                                     dept_name = lvctboard.dept_name,
                                     lvct_model = lvctboard.lvct_model,
                                     lvct_manufacture_batch_no = lvctboard.lvct_manufacture_batch_no,
                                     lvct_type_testing_cert_no = lvctboard.lvct_type_testing_cert_no,
                                     lvct_manufacture_date = lvctboard.lvct_manufacture_date,
                                     user_id = lvctboard.user_id)
    db.add(db_lvctboard)
    db.commit()
    db.refresh(db_lvctboard)
    return db_lvctboard