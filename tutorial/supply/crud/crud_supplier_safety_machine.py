from uuid import UUID
import datetime

from sqlalchemy.orm import Session
from sqlalchemy import delete,select

import models as models
import schemas as schemas

def get_safety_machines(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.SupplierSafetyMachine).offset(skip).limit(limit).all()

def create_safety_machine(db:Session, 
                         safety_machine: schemas.SafetyMachineCreate)->models.SupplierSafetyMachine:
    obj = models.SupplierSafetyMachine(**safety_machine.dict())
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj

def create_safety_machines(db: Session, 
                          safety_machines: list[schemas.SafetyMachineCreate]
                         )->list[models.SupplierSafetyMachine]:
    objects = [models.SupplierSafetyMachine(**safety_machine.dict()) for safety_machine in safety_machines]
    db.bulk_save_objects(objects)
    db.commit()
    return objects

def delete_safety_machine(db: Session, safety_machine_id: UUID)->models.SupplierSafetyMachine:
    statement = delete(models.SupplierSafetyMachine).where(models.SupplierSafetyMachine.safety_machine_id==str(safety_machine_id),
                                                          models.SupplierSafetyMachine.data_state==schemas.DataState.Submited)
    db_obj = db.execute(statement)
    db.commit()
    return db_obj.rowcount

def delete_safety_machine_on_days(db: Session, num_days:int = 1)->int:
    end_date = datetime.datetime.now()
    start_date = end_date - datetime.timedelta(days=num_days)
    statement = delete(models.SupplierSafetyMachine).where(models.SupplierSafetyMachine.create_time > start_date,
                                                    models.SupplierSafetyMachine.create_time <= end_date,
                                                    models.SupplierSafetyMachine.data_state==schemas.DataState.Submited )
    safety_machines = db.execute(statement)
    db.commit()
    return safety_machines.rowcount
