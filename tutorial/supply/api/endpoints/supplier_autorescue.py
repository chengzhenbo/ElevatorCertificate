from typing import List, Any
from uuid import UUID

from fastapi import APIRouter, Depends, UploadFile, status, HTTPException
from sqlalchemy.orm import Session
from io import BytesIO

from core.excel_reader import read_supplier_data, SupplierType
import crud.crud_supplier_autorescue as crud_supplier_autorescue
import schemas as schemas
from api import deps

router = APIRouter()

@router.get('/auto_rescues', response_model=List[schemas.AutoRescue])
def read_auto_rescues(db: Session = Depends(deps.get_db),
                      skip: int = 0,
                      limit: int = 100)->Any:
    objs = crud_supplier_autorescue.get_auto_rescue(db=db, skip=skip, limit=limit)
    return objs