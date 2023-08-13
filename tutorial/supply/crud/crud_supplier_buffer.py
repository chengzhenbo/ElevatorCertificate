from uuid import UUID
import datetime

from sqlalchemy.orm import Session
from sqlalchemy import delete,select

import models as models
import schemas as schemas

def get_buffers(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.SupplierBuffer).offset(skip).limit(limit).all()

def create_buffer(db:Session, 
                  buffer: schemas.BufferCreate)->models.SupplierBuffer:
    obj = models.SupplierBuffer(**buffer.dict())
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj

def create_buffers(db: Session, 
                   buffers: list[schemas.BufferCreate]
                   )->list[models.SupplierBuffer]:
    objects = [models.SupplierBuffer(**buffer.dict()) for buffer in buffers]
    db.bulk_save_objects(objects)
    db.commit()
    return objects

def delete_buffer(db: Session, buffer_id: UUID)->models.SupplierBuffer:
    statement = delete(models.SupplierBuffer).where(models.SupplierBuffer.buffer_id==str(buffer_id),
                                                    models.SupplierBuffer.data_state==schemas.DataState.Submited)
    db_obj = db.execute(statement)
    db.commit()
    return db_obj

def delete_buffer_on_days(db: Session, num_days:int = 1)->int:
    end_date = datetime.datetime.now()
    start_date = end_date - datetime.timedelta(days=num_days)
    statement = delete(models.SupplierBuffer).where(models.SupplierBuffer.create_time > start_date,
                                                    models.SupplierBuffer.create_time <= end_date,
                                                    models.SupplierBuffer.data_state==schemas.DataState.Submited )
    buffers = db.execute(statement)
    db.commit()
    return buffers.rowcount
