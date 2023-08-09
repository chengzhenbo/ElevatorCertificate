from typing import List, Any
from uuid import UUID

from fastapi import APIRouter, Depends, UploadFile, status, HTTPException
from sqlalchemy.orm import Session
from io import BytesIO

from core.excel_reader import read_supplier_data, SupplierType
import crud.crud_supplier_ropehead as crud_supplier_ropehead
import schemas as schemas
from api import deps

router = APIRouter()

@router.get('/rope_heads', response_model=List[schemas.RopeHead])
def read_rope_heads(db: Session = Depends(deps.get_db),
                      skip: int = 0,
                      limit: int = 100)->Any:
    rope_heads = crud_supplier_ropehead.get_rope_head(db=db, skip=skip, limit=limit)
    return rope_heads