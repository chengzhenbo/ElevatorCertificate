from uuid import UUID
import datetime

from sqlalchemy.orm import Session
from sqlalchemy import delete,select

import models as models
import schemas as schemas

def get_wire_ropes(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.SupplierWireRope).offset(skip).limit(limit).all()

def create_wire_rope(db:Session, 
                         wire_rope: schemas.WireRopeCreate)->models.SupplierWireRope:
    obj = models.SupplierWireRope(**wire_rope.dict())
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj

def create_wire_ropes(db: Session, 
                          wire_ropes: list[schemas.WireRopeCreate]
                         )->list[models.SupplierWireRope]:
    objects = [models.SupplierWireRope(**wire_rope.dict()) for wire_rope in wire_ropes]
    db.bulk_save_objects(objects)
    db.commit()
    return objects

def delete_wire_rope(db: Session, wire_rope_id: UUID)->models.SupplierWireRope:
    statement = delete(models.SupplierWireRope).where(models.SupplierWireRope.wire_rope_id==str(wire_rope_id),
                                                          models.SupplierWireRope.data_state==schemas.DataState.Submited)
    db_obj = db.execute(statement)
    db.commit()
    return db_obj.rowcount

def delete_wire_rope_on_days(db: Session, num_days:int = 1)->int:
    end_date = datetime.datetime.now()
    start_date = end_date - datetime.timedelta(days=num_days)
    statement = delete(models.SupplierWireRope).where(models.SupplierWireRope.create_time > start_date,
                                                    models.SupplierWireRope.create_time <= end_date,
                                                    models.SupplierWireRope.data_state==schemas.DataState.Submited )
    wire_ropes = db.execute(statement)
    db.commit()
    return wire_ropes.rowcount
