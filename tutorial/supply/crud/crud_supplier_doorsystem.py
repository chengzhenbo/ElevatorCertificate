from uuid import UUID
import datetime

from sqlalchemy.orm import Session
from sqlalchemy import delete,select

import models as models
import schemas as schemas

def get_door_systems(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.ModelSupplierKongZhiGuiMenXiTong).offset(skip).limit(limit).all()

def create_door_system(db:Session, 
                         door_system: schemas.DoorSystemCreate)->models.ModelSupplierKongZhiGuiMenXiTong:
    obj = models.ModelSupplierKongZhiGuiMenXiTong(**door_system.dict())
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj

def create_door_systems(db: Session, 
                          door_systems: list[schemas.DoorSystemCreate]
                         )->list[models.ModelSupplierKongZhiGuiMenXiTong]:
    objects = [models.ModelSupplierKongZhiGuiMenXiTong(**door_system.dict()) for door_system in door_systems]
    db.bulk_save_objects(objects)
    db.commit()
    return objects

def delete_door_system(db: Session, door_system_id: UUID)->models.ModelSupplierKongZhiGuiMenXiTong:
    statement = delete(models.ModelSupplierKongZhiGuiMenXiTong).where(models.ModelSupplierKongZhiGuiMenXiTong.door_system_id==str(door_system_id),
                                                          models.ModelSupplierKongZhiGuiMenXiTong.data_state==schemas.DataState.Submited)
    db_obj = db.execute(statement)
    db.commit()
    return db_obj

def delete_door_system_on_days(db: Session, num_days:int = 1)->int:
    end_date = datetime.datetime.now()
    start_date = end_date - datetime.timedelta(days=num_days)
    statement = delete(models.ModelSupplierKongZhiGuiMenXiTong).where(models.ModelSupplierKongZhiGuiMenXiTong.create_time > start_date,
                                                    models.ModelSupplierKongZhiGuiMenXiTong.create_time <= end_date,
                                                    models.ModelSupplierKongZhiGuiMenXiTong.data_state==schemas.DataState.Submited )
    door_systems = db.execute(statement)
    db.commit()
    return door_systems.rowcount