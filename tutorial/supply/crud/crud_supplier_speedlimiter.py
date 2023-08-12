from uuid import UUID
import datetime

from sqlalchemy.orm import Session
from sqlalchemy import delete

import models as models
import schemas as schemas

def get_speed_limiters(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.SupplierSpeedLimiter).offset(skip).limit(limit).all()

def create_speed_limiters(db: Session, 
                          safe_brakes: list[schemas.SpeedLimiterCreate]
                         )->list[models.SupplierSpeedLimiter]:
    
    objects = [models.SupplierSpeedLimiter(**safe_brake.dict()) for safe_brake in safe_brakes]
    db.bulk_save_objects(objects)
    db.commit()
    return objects