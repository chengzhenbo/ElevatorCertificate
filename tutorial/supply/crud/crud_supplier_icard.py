from uuid import UUID
import datetime

from sqlalchemy.orm import Session
from sqlalchemy import delete

import models as models
import schemas as schemas

def get_ic_card(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.SupplierIcCard).offset(skip).limit(limit).all()

def create_ic_card(db: Session, 
                   icard: schemas.IcCardCreate
                   )->models.SupplierIcCard:
    db_object = models.SupplierIcCard(contract_no = icard.contract_no,
                                    icard_model = icard.icard_model,
                                    icard_no = icard.icard_no,
                                    user_id = icard.user_id,
                                    create_time = datetime.datetime.now(),
                                    update_time = datetime.datetime.now())
    db.add(db_object)
    db.commit()
    db.refresh(db_object)
    return db_object

def delete_ic_card(db: Session, icard_id: UUID):
    ic_card = db.query(models.SupplierIcCard).get(str(icard_id))
    db.delete(ic_card)
    db.commit()

def delete_ic_card_on_days(db: Session, num_days:int = 1):
    end_date = datetime.datetime.now()
    start_date = end_date - datetime.timedelta(days=num_days)
    statement = delete(models.SupplierIcCard).where(models.SupplierIcCard.create_time > start_date,
                                                    models.SupplierIcCard.create_time <= end_date )
    db.execute(statement)
    db.commit()