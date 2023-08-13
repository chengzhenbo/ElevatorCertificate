from typing import List, Any
from uuid import UUID

from fastapi import APIRouter, Depends, UploadFile, status, HTTPException
from sqlalchemy.orm import Session
from io import BytesIO

from core.excel_reader import read_supplier_data, SupplierType
import crud as crud
import schemas as schemas
from api import deps

router = APIRouter()

@router.get('/brakes', response_model=List[schemas.BrakeMachine])
def read_brakes(db: Session = Depends(deps.get_db),
                     skip: int = 0,
                     limit: int = 100)->Any:
    objs = crud.crud_supplier_brake_machine.get_brake_machines(db=db, skip=skip, limit=limit)
    return objs

@router.get('/safeties', response_model=List[schemas.SafetyMachine])
def read_safeties(db: Session = Depends(deps.get_db),
                     skip: int = 0,
                     limit: int = 100)->Any:
    objs = crud.crud_supplier_safety_machine.get_safety_machines(db=db, skip=skip, limit=limit)
    return objs

@router.get('/tractions', response_model=List[schemas.TractionMachine])
def read_tractions(db: Session = Depends(deps.get_db),
                     skip: int = 0,
                     limit: int = 100)->Any:
    objs = crud.crud_supplier_traction_machine.get_traction_machines(db=db, skip=skip, limit=limit)
    return objs

@router.post('/machines', 
             response_model = schemas.SupplierMachines, 
             status_code=status.HTTP_201_CREATED)
async def upload_machines(file: UploadFile, 
                            db: Session = Depends(deps.get_db)):
    if file.filename.endswith('.xlsx'):
        f = await file.read()
        excelfile = BytesIO(f)
        tractions_df = read_supplier_data(supplier_type=SupplierType.ZHUJI_QUDONG, 
                                               path = excelfile)
        safeties_df = read_supplier_data(supplier_type=SupplierType.ZHUJI_YIDONGBAOHU, 
                                               path = excelfile)
        brakes_df = read_supplier_data(supplier_type=SupplierType.ZHUJI_ZHIDONG, 
                                               path = excelfile)
        if tractions_df.valid_dataframe.empty:
            raise HTTPException(status_code=400,
                                detail="主机的驱动装置有效数据为空.")
        if safeties_df.valid_dataframe.empty:
            raise HTTPException(status_code=400,
                                detail="主机的移动保护装置有效数据为空.")
        if brakes_df.valid_dataframe.empty:
            raise HTTPException(status_code=400,
                                detail="主机的制动器有效数据为空.")
        traction_records = tractions_df.valid_dataframe.to_dict('records')
        safety_records = safeties_df.valid_dataframe.to_dict('records')
        brake_records = brakes_df.valid_dataframe.to_dict('records')
        traction_machines,safety_machines,brake_machines = [],[],[]
        for record in traction_records:
            traction_machine = schemas.TractionMachineCreate(**record)
            db_obj = crud.crud_supplier_traction_machine.create_traction_machine(db=db,
                                                        traction_machine = traction_machine)
            if not db_obj:
                raise HTTPException(status_code=404,
                                    detail="主机的驱动装置数据未能正常写入数据库.")
            traction_machines.append(db_obj)
        for record in brake_records:
            brake_machine = schemas.BrakeMachineCreate(**record)
            db_obj = crud.crud_supplier_brake_machine.create_brake_machine(db=db,
                                                        brake_machine = brake_machine)
            if not db_obj:
                raise HTTPException(status_code=404,
                                    detail="主机的制动装置数据未能正常写入数据库.")
            safety_machines.append(db_obj)
        for record in safety_records:
            safety_machine = schemas.SafetyMachineCreate(**record)
            db_obj = crud.crud_supplier_safety_machine.create_safety_machine(db=db,
                                                        safety_machine = safety_machine)
            if not db_obj:
                raise HTTPException(status_code=404,
                                    detail="主机的安全装置数据未能正常写入数据库.")
            brake_machines.append(db_obj)
        return {"traction_machines":traction_machines, 
                "brake_machines":brake_machines,
                "safety_machines":safety_machines}
    else:
        raise HTTPException(status_code=404, detail="File can not open")

@router.delete('/delete_machines/{num_days}')
def delete_machines_by_numdays(db: Session = Depends(deps.get_db), num_days:int = 1):
    count_traction, count_brake, count_safety = 0, 0, 0
    count_traction = crud.crud_supplier_traction_machine.delete_traction_machine_on_days(db=db, num_days = num_days)
    count_brake = crud.crud_supplier_brake_machine.delete_brake_machine_on_days(db=db, num_days = num_days)
    count_safety = crud.crud_supplier_safety_machine.delete_safety_machine_on_days(db=db, num_days = num_days)
    
    return {"num of tractions deleted": count_traction,
            "num of brakes deleted": count_brake,
            "num of safeties deleted": count_safety}
