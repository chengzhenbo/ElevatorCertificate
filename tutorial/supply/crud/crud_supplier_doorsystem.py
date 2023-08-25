from uuid import UUID
import datetime

from sqlalchemy.orm import Session
from sqlalchemy import delete,select

import models as models
import schemas as schemas

def get_door_systems(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.ModelSupplierMenXiTong).offset(skip).limit(limit).all()

def create_door_system(db:Session, 
                         door_system: schemas.DoorSystemCreate)->models.ModelSupplierMenXiTong:
    obj = models.ModelSupplierMenXiTong(**door_system.dict())
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj

def create_door_systems(db: Session, 
                          door_systems: list[schemas.DoorSystemCreate]
                         )->list[models.ModelSupplierMenXiTong]:
    objects = [models.ModelSupplierMenXiTong(**door_system.dict()) for door_system in door_systems]
    db.bulk_save_objects(objects)
    db.commit()
    return objects

def delete_door_system(db: Session, door_system_id: UUID)->models.ModelSupplierMenXiTong:
    statement = delete(models.ModelSupplierMenXiTong).where(models.ModelSupplierMenXiTong.door_system_id==str(door_system_id),
                                                          models.ModelSupplierMenXiTong.data_state==schemas.DataState.Submited)
    db_obj = db.execute(statement)
    db.commit()
    return db_obj

def delete_door_system_on_days(db: Session, num_days:int = 1)->int:
    end_date = datetime.datetime.now()
    start_date = end_date - datetime.timedelta(days=num_days)
    statement = delete(models.ModelSupplierMenXiTong).where(models.ModelSupplierMenXiTong.create_time > start_date,
                                                    models.ModelSupplierMenXiTong.create_time <= end_date,
                                                    models.ModelSupplierMenXiTong.data_state==schemas.DataState.Submited )
    door_systems = db.execute(statement)
    db.commit()
    return door_systems.rowcount