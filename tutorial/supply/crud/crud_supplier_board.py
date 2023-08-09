from uuid import UUID
import datetime

from sqlalchemy.orm import Session
from sqlalchemy import delete

import models as models
import schemas as schemas

def get_smart_boards(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.SupplierSmartBoard).offset(skip).limit(limit).all()

def get_lvct_boards(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.SupplierLvctBoard).offset(skip).limit(limit).all()

def create_smart_board(db: Session, 
                       smartboard: schemas.SmartBoardCreate)->models.SupplierSmartBoard:
    db_smartboard = models.SupplierSmartBoard(contract_no = smartboard.contract_no,
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

def create_lvct_board(db: Session, 
                      lvctboard: schemas.LvctBoardCreate)->models.SupplierLvctBoard:
    db_lvctboard = models.SupplierLvctBoard(contract_no = lvctboard.contract_no,
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

def delete_smart_board(db: Session, smart_board_id: UUID):
    smart_board = db.query(models.SupplierSmartBoard).get(str(smart_board_id))
    print("smart_board = ", smart_board)
    db.delete(smart_board)
    db.commit()

def delete_lvct_board(db: Session, lvct_board_id: UUID):
    lvct_board = db.query(models.SupplierLvctBoard).get(str(lvct_board_id))
    db.delete(lvct_board)
    db.commit()

def delete_smart_board_on_days(db: Session, num_days:int = 1):
    end_date = datetime.datetime.now()
    start_date = datetime.datetime.now() - datetime.timedelta(days=num_days)
    statement = delete(models.SupplierSmartBoard).where(models.SupplierSmartBoard.create_time > start_date,
                                                 models.SupplierSmartBoard.create_time <= end_date )
    db.execute(statement)
    db.commit()

def delete_lvct_board_on_days(db: Session, num_days:int = 1):
    end_date = datetime.datetime.now()
    start_date = end_date - datetime.timedelta(days=num_days)
    statement = delete(models.SupplierLvctBoard).where(models.SupplierLvctBoard.create_time > start_date,
                                                 models.SupplierLvctBoard.create_time <= end_date )
    db.execute(statement)
    db.commit()