from uuid import UUID
import datetime

from sqlalchemy.orm import Session
from sqlalchemy import delete

import models as models
import schemas as schemas

def get_rope_head(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.SupplierRopeHead).offset(skip).limit(limit).all()

def create_rope_head(db: Session, 
                       ropehead: schemas.RopeHeadCreate)->models.SupplierRopeHead:
    db_ropehead = models.SupplierRopeHead(contract_no = ropehead.contract_no,
                                          dept_name = ropehead.dept_name,
                                          ropehc_model = ropehead.ropehc_model,
                                          ropehc_manufacture_batch_no = ropehead.ropehc_manufacture_batch_no,
                                          ropehc_type_testing_cert_no = ropehead.ropehc_type_testing_cert_no,
                                          ropehc_manufacture_date = ropehead.ropehc_manufacture_date,
                                          user_id = ropehead.user_id,
                                          create_time = datetime.datetime.now(),
                                          update_time = datetime.datetime.now())
    db.add(db_ropehead)
    db.commit()
    db.refresh(db_ropehead)
    return db_ropehead

def delete_rope_head(db: Session, rope_head_id: UUID):
    rope_head = db.query(models.SupplierRopeHead).get(str(rope_head_id))
    db.delete(rope_head)
    db.commit()

def delete_rope_head_on_days(db: Session, num_days:int = 1):
    end_date = datetime.datetime.now()
    start_date = datetime.datetime.now() - datetime.timedelta(days=num_days)
    statement = delete(models.SupplierRopeHead).where(models.SupplierRopeHead.create_time > start_date,
                                                 models.SupplierRopeHead.create_time <= end_date )
    db.execute(statement)
    db.commit()