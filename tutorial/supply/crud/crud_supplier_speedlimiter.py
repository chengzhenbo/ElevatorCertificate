from uuid import UUID
import datetime

from sqlalchemy.orm import Session
from sqlalchemy import delete,select

import models as models
import schemas as schemas

def get_speed_limiters(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.SupplierSpeedLimiter).offset(skip).limit(limit).all()

def create_speed_limiter(db:Session, 
                         speed_limiter: schemas.SpeedLimiterCreate)->models.SupplierSpeedLimiter:
    obj = models.SupplierSpeedLimiter(**speed_limiter.dict())
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj

def create_speed_limiters(db: Session, 
                          speed_limiters: list[schemas.SpeedLimiterCreate]
                         )->list[models.SupplierSpeedLimiter]:
    objects = [models.SupplierSpeedLimiter(**speed_limiter.dict()) for speed_limiter in speed_limiters]
    db.bulk_save_objects(objects)
    db.commit()
    return objects

def delete_speed_limiter(db: Session, speed_limiter_id: UUID)->models.SupplierSpeedLimiter:
    statement = delete(models.SupplierSpeedLimiter).where(models.SupplierSpeedLimiter.speed_limiter_id==str(speed_limiter_id),
                                                          models.SupplierSpeedLimiter.data_state==schemas.DataState.Submited)
    db_obj = db.execute(statement)
    db.commit()
    return db_obj

def delete_speed_limiter_on_days(db: Session, num_days:int = 1)->int:
    end_date = datetime.datetime.now()
    start_date = end_date - datetime.timedelta(days=num_days)
    statement = delete(models.SupplierSpeedLimiter).where(models.SupplierSpeedLimiter.create_time > start_date,
                                                    models.SupplierSpeedLimiter.create_time <= end_date,
                                                    models.SupplierSpeedLimiter.data_state==schemas.DataState.Submited )
    speed_limiters = db.execute(statement)
    db.commit()
    return speed_limiters.rowcount
