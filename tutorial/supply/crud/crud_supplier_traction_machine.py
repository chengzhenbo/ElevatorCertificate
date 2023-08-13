from uuid import UUID
import datetime

from sqlalchemy.orm import Session
from sqlalchemy import delete,select

import models as models
import schemas as schemas

def get_traction_machines(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.SupplierTractionMachine).offset(skip).limit(limit).all()

def create_traction_machine(db:Session, 
                         traction_machine: schemas.TractionMachineCreate)->models.SupplierTractionMachine:
    obj = models.SupplierTractionMachine(**traction_machine.dict())
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj

def create_traction_machines(db: Session, 
                          traction_machines: list[schemas.TractionMachineCreate]
                         )->list[models.SupplierTractionMachine]:
    objects = [models.SupplierTractionMachine(**traction_machine.dict()) for traction_machine in traction_machines]
    db.bulk_save_objects(objects)
    db.commit()
    return objects

def delete_traction_machine(db: Session, traction_machine_id: UUID)->models.SupplierTractionMachine:
    statement = delete(models.SupplierTractionMachine).where(models.SupplierTractionMachine.traction_machine_id==str(traction_machine_id),
                                                          models.SupplierTractionMachine.data_state==schemas.DataState.Submited)
    db_obj = db.execute(statement)
    db.commit()
    return db_obj.rowcount

def delete_traction_machine_on_days(db: Session, num_days:int = 1)->int:
    end_date = datetime.datetime.now()
    start_date = end_date - datetime.timedelta(days=num_days)
    statement = delete(models.SupplierTractionMachine).where(models.SupplierTractionMachine.create_time > start_date,
                                                    models.SupplierTractionMachine.create_time <= end_date,
                                                    models.SupplierTractionMachine.data_state==schemas.DataState.Submited )
    traction_machines = db.execute(statement)
    db.commit()
    return traction_machines.rowcount