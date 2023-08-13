from uuid import UUID
import datetime

from sqlalchemy.orm import Session
from sqlalchemy import delete,select

import models as models
import schemas as schemas

def get_brake_machines(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.SupplierBrakeMachine).offset(skip).limit(limit).all()

def create_brake_machine(db:Session, 
                         brake_machine: schemas.BrakeMachineCreate)->models.SupplierBrakeMachine:
    obj = models.SupplierBrakeMachine(**brake_machine.dict())
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj

def create_brake_machines(db: Session, 
                          brake_machines: list[schemas.BrakeMachineCreate]
                         )->list[models.SupplierBrakeMachine]:
    objects = [models.SupplierBrakeMachine(**brake_machine.dict()) for brake_machine in brake_machines]
    db.bulk_save_objects(objects)
    db.commit()
    return objects

def delete_brake_machine(db: Session, brake_machine_id: UUID)->models.SupplierBrakeMachine:
    statement = delete(models.SupplierBrakeMachine).where(models.SupplierBrakeMachine.brake_machine_id==str(brake_machine_id),
                                                          models.SupplierBrakeMachine.data_state==schemas.DataState.Submited)
    db_obj = db.execute(statement)
    db.commit()
    return db_obj.rowcount

def delete_brake_machine_on_days(db: Session, num_days:int = 1)->int:
    end_date = datetime.datetime.now()
    start_date = end_date - datetime.timedelta(days=num_days)
    statement = delete(models.SupplierBrakeMachine).where(models.SupplierBrakeMachine.create_time > start_date,
                                                    models.SupplierBrakeMachine.create_time <= end_date,
                                                    models.SupplierBrakeMachine.data_state==schemas.DataState.Submited )
    brake_machines = db.execute(statement)
    db.commit()
    return brake_machines.rowcount
