from uuid import UUID
import datetime

from sqlalchemy.orm import Session
from sqlalchemy import delete,select

import models as models
import schemas as schemas

def get_control_cabinets(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.ModelSupplierKongZhiGui).offset(skip).limit(limit).all()

def create_control_cabinet(db:Session, 
                         control_cabinet: schemas.ControlCabinetCreate)->models.ModelSupplierKongZhiGui:
    obj = models.ModelSupplierKongZhiGui(**control_cabinet.dict())
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj

def create_control_cabinets(db: Session, 
                          control_cabinets: list[schemas.ControlCabinetCreate]
                         )->list[models.ModelSupplierKongZhiGui]:
    objects = [models.ModelSupplierKongZhiGui(**control_cabinet.dict()) for control_cabinet in control_cabinets]
    db.bulk_save_objects(objects)
    db.commit()
    return objects

def delete_control_cabinet(db: Session, control_cabinet_id: UUID)->models.ModelSupplierKongZhiGui:
    statement = delete(models.ModelSupplierKongZhiGui).where(models.ModelSupplierKongZhiGui.control_cabinet_id==str(control_cabinet_id),
                                                          models.ModelSupplierKongZhiGui.data_state==schemas.DataState.Submited)
    db_obj = db.execute(statement)
    db.commit()
    return db_obj

def delete_control_cabinet_on_days(db: Session, num_days:int = 1)->int:
    end_date = datetime.datetime.now()
    start_date = end_date - datetime.timedelta(days=num_days)
    statement = delete(models.ModelSupplierKongZhiGui).where(models.ModelSupplierKongZhiGui.create_time > start_date,
                                                    models.ModelSupplierKongZhiGui.create_time <= end_date,
                                                    models.ModelSupplierKongZhiGui.data_state==schemas.DataState.Submited )
    control_cabinets = db.execute(statement)
    db.commit()
    return control_cabinets.rowcount