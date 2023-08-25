from typing import List, Any
from uuid import UUID

from fastapi import APIRouter, Depends, UploadFile, status, HTTPException
from sqlalchemy.orm import Session
from io import BytesIO

from core.excel_reader import read_supplier_data, SupplierType
import crud.crud_supplier_doorsystem as crud_supplier_doorsystem
import schemas as schemas
from api import deps

router = APIRouter()

@router.get('/doorsystems', response_model=List[schemas.DoorSystem])
def read_doorsystems(db: Session = Depends(deps.get_db),
                     skip: int = 0,
                     limit: int = 100)->Any:
    objs = crud_supplier_doorsystem.get_door_systems(db=db, 
                                                          skip=skip, 
                                                          limit=limit)
    return objs

@router.post('/door_systems', 
             response_model = schemas.ListDoorSystems, 
             status_code=status.HTTP_201_CREATED)
async def upload_door_systems(file: UploadFile, 
                              db: Session = Depends(deps.get_db)):
    if file.filename.endswith('.xlsx'):
        f = await file.read()
        excelfile = BytesIO(f)
        door_systems_df1 = read_supplier_data(supplier_type=SupplierType.MENXITONG_1, 
                                               path = excelfile)
        door_systems_df2 = read_supplier_data(supplier_type=SupplierType.MENXITONG_2, 
                                               path = excelfile)
        door_systems_df3 = read_supplier_data(supplier_type=SupplierType.MENXITONG_3, 
                                               path = excelfile)
        door_systems_df4 = read_supplier_data(supplier_type=SupplierType.MENXITONG_4, 
                                               path = excelfile)
        door_systems_df5 = read_supplier_data(supplier_type=SupplierType.MENXITONG_5, 
                                               path = excelfile)
        door_systems_df6 = read_supplier_data(supplier_type=SupplierType.MENXITONG_6, 
                                               path = excelfile)
        door_systems = []
        if not door_systems_df1.valid_dataframe.empty:
            records = door_systems_df1.valid_dataframe.to_dict('records')
            for record in records:
                door_system = schemas.DoorSystemCreate(**record,
                                                       remark=schemas.DoorSystemType.LandingDoor)
                db_obj = crud_supplier_doorsystem.create_door_system(db=db,
                                                                    door_system = door_system)
                if not db_obj:
                    raise HTTPException(status_code=404,
                                        detail="门系统-层门数据未能正常写入数据库.")
                door_systems.append(db_obj)
        if not door_systems_df2.valid_dataframe.empty:
            records = door_systems_df2.valid_dataframe.to_dict('records')
            for record in records:
                door_system = schemas.DoorSystemCreate(**record,
                                                       remark=schemas.DoorSystemType.FireDoor)
                db_obj = crud_supplier_doorsystem.create_door_system(db=db,
                                                                    door_system = door_system)
                if not db_obj:
                    raise HTTPException(status_code=404,
                                        detail="门系统-防火门数据未能正常写入数据库.")
                door_systems.append(db_obj)
        if not door_systems_df3.valid_dataframe.empty:
            records = door_systems_df3.valid_dataframe.to_dict('records')
            for record in records:
                door_system = schemas.DoorSystemCreate(**record,
                                                       remark=schemas.DoorSystemType.GlassCarDoor)
                db_obj = crud_supplier_doorsystem.create_door_system(db=db,
                                                                    door_system = door_system)
                if not db_obj:
                    raise HTTPException(status_code=404,
                                        detail="门系统-玻璃轿门数据未能正常写入数据库.")
                door_systems.append(db_obj)
        if not door_systems_df4.valid_dataframe.empty:
            records = door_systems_df4.valid_dataframe.to_dict('records')
            for record in records:
                door_system = schemas.DoorSystemCreate(**record,
                                                       remark=schemas.DoorSystemType.GlassCarWall)
                db_obj = crud_supplier_doorsystem.create_door_system(db=db,
                                                                    door_system = door_system)
                if not db_obj:
                    raise HTTPException(status_code=404,
                                        detail="门系统-玻璃轿壁数据未能正常写入数据库.")
                door_systems.append(db_obj)
        if not door_systems_df5.valid_dataframe.empty:
            records = door_systems_df5.valid_dataframe.to_dict('records')
            for record in records:
                door_system = schemas.DoorSystemCreate(**record,
                                                       remark=schemas.DoorSystemType.HallDoorLock)
                db_obj = crud_supplier_doorsystem.create_door_system(db=db,
                                                                    door_system = door_system)
                if not db_obj:
                    raise HTTPException(status_code=404,
                                        detail="门系统-厅门锁数据未能正常写入数据库.")
                door_systems.append(db_obj)
        if not door_systems_df6.valid_dataframe.empty:
            records = door_systems_df6.valid_dataframe.to_dict('records')
            for record in records:
                door_system = schemas.DoorSystemCreate(**record,
                                                       remark=schemas.DoorSystemType.CarDoorLock)
                db_obj = crud_supplier_doorsystem.create_door_system(db=db,
                                                                    door_system = door_system)
                if not db_obj:
                    raise HTTPException(status_code=404,
                                        detail="门系统-轿门锁数据未能正常写入数据库.")
                door_systems.append(db_obj)
       
        return {"door_systems":door_systems}
    else:
        raise HTTPException(status_code=404, detail="File can not open")

@router.delete('/delete_door_system/{door_system_id}', 
               status_code=status.HTTP_204_NO_CONTENT)
def delete_door_system_by_id(door_system_id:UUID, db: Session = Depends(deps.get_db)):
    db_obj = crud_supplier_doorsystem.delete_door_system(db=db, 
                                                         door_system_id = door_system_id)
    if not db_obj:
        raise HTTPException(status_code=404,
                            detail="门系统数据未能正常从数据库中删除.")
    
@router.delete('/delete_door_systems/{num_days}')
def delete_door_system_by_numdays(db: Session = Depends(deps.get_db), num_days:int = 1):
    count = crud_supplier_doorsystem.delete_door_system_on_days(db=db, num_days = num_days)
    if count > 0:
        return {"num of objs deleted": count}
    else:
        raise HTTPException(status_code=404,
                            detail="没有删除数据.")
