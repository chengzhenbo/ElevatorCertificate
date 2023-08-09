from uuid import UUID
import datetime

from sqlalchemy.orm import Session
from sqlalchemy import delete

import models as models
import schemas as schemas

def get_auto_rescue(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.SupplierAutoRescue).offset(skip).limit(limit).all()

def create_auto_rescue(db: Session, 
                       autorescue: schemas.AutoRescueCreate)->models.SupplierAutoRescue:
    db_autorescue = models.SupplierAutoRescue(contract_no = autorescue.contract_no,
                                              dept_name = autorescue.dept_name,
                                              auto_rescue_model = autorescue.auto_rescue_model,
                                              auto_rescue_no = autorescue.auto_rescue_no,
                                              user_id = autorescue.user_id,
                                              create_time = datetime.datetime.now(),
                                              update_time = datetime.datetime.now())
    db.add(db_autorescue)
    db.commit()
    db.refresh(db_autorescue)
    return db_autorescue

def delete_auto_rescue(db: Session, auto_rescue_id: UUID):
    auto_rescue = db.query(models.SupplierAutoRescue).get(str(auto_rescue_id))
    db.delete(auto_rescue)
    db.commit()

def delete_auto_rescue_on_days(db: Session, num_days:int = 1):
    end_date = datetime.datetime.now()
    start_date = datetime.datetime.now() - datetime.timedelta(days=num_days)
    statement = delete(models.SupplierAutoRescue).where(models.SupplierAutoRescue.create_time > start_date,
                                                        models.SupplierAutoRescue.create_time <= end_date )
    db.execute(statement)
    db.commit()