from uuid import UUID
import datetime

from sqlalchemy.orm import Session
from sqlalchemy import delete

import models as models
import schemas as schemas

def get_safe_brake(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.SupplierSafeBrake).offset(skip).limit(limit).all()

def create_safe_brake(db: Session, 
                      safe_brake: schemas.SafeBrakeCreate
                     )->models.SupplierSafeBrake:
    db_object = models.SupplierSafeBrake(contract_no = safe_brake.contract_no,
                                        user_name = safe_brake.user_name,
                                        dept_name = safe_brake.dept_name,
                                        product_type_name = safe_brake.product_type_name,
                                        product_model = safe_brake.product_model,
                                        product_speed = safe_brake.product_speed,
                                        product_no = safe_brake.product_no,
                                        product_testing_cert_no = safe_brake.product_testing_cert_no,
                                        manufacture_date = safe_brake.manufacture_date,
                                        user_id = safe_brake.user_id,
                                        create_time = datetime.datetime.now(),
                                        update_time = datetime.datetime.now())
    db.add(db_object)
    db.commit()
    db.refresh(db_object)
    return db_object

def delete_safe_brake(db: Session, safe_brake_id: UUID):
    safe_brake = db.query(models.SupplierSafeBrake).get(str(safe_brake_id))
    db.delete(safe_brake)
    db.commit()

def delete_safe_brake_on_days(db: Session, num_days:int = 1):
    end_date = datetime.datetime.now()
    start_date = end_date - datetime.timedelta(days=num_days)
    statement = delete(models.SupplierSafeBrake).where(models.SupplierSafeBrake.create_time > start_date,
                                                    models.SupplierSafeBrake.create_time <= end_date )
    db.execute(statement)
    db.commit()