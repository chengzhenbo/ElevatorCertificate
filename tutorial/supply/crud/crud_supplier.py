from uuid import UUID
import datetime

from sqlalchemy.orm import Session
from sqlalchemy import delete

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
                                       user_id = smartboard.user_id,
                                       create_time = datetime.datetime.now(),
                                       update_time = datetime.datetime.now())
    db.add(db_smartboard)
    db.commit()
    db.refresh(db_smartboard)
    return db_smartboard

def delete_smart_board(db: Session, smart_board_id: UUID):
    smart_board = db.query(SupplierSmartBoard).filter(SupplierSmartBoard.smartb_id == smart_board_id)
    db.delete(smart_board)
    db.commit()

def delete_smart_board_on_days(db: Session, num_days:int = 1):
    end_date = datetime.datetime.now()
    start_date = datetime.datetime.now() - datetime.timedelta(days=num_days)
    statement = delete(SupplierSmartBoard).where(SupplierSmartBoard.create_time > start_date,
                                                 SupplierSmartBoard.create_time <= end_date )
    db.execute(statement)
    db.commit()

def create_lvct_board(db: Session, 
                      lvctboard: schemas.LvctBoardCreate)->SupplierLvctBoard:
    db_lvctboard = SupplierLvctBoard(contract_no = lvctboard.contract_no,
                                     dept_name = lvctboard.dept_name,
                                     lvct_model = lvctboard.lvct_model,
                                     lvct_manufacture_batch_no = lvctboard.lvct_manufacture_batch_no,
                                     lvct_type_testing_cert_no = lvctboard.lvct_type_testing_cert_no,
                                     lvct_manufacture_date = lvctboard.lvct_manufacture_date,
                                     user_id = lvctboard.user_id,
                                     create_time = datetime.datetime.now(),
                                     update_time = datetime.datetime.now())
    db.add(db_lvctboard)
    db.commit()
    db.refresh(db_lvctboard)
    return db_lvctboard

def delete_lvct_board(db: Session, lvct_board_id: UUID):
    lvct_board = db.query(SupplierLvctBoard).filter(SupplierLvctBoard.lvctb_id == lvct_board_id)
    db.delete(lvct_board)
    db.commit()

def delete_lvct_board_on_days(db: Session, num_days:int = 1):
    end_date = datetime.datetime.now()
    start_date = datetime.datetime.now() - datetime.timedelta(days=num_days)
    statement = delete(SupplierLvctBoard).where(SupplierLvctBoard.create_time > start_date,
                                                 SupplierLvctBoard.create_time <= end_date )
    db.execute(statement)
    db.commit()