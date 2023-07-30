from fastapi import FastAPI,UploadFile,HTTPException
import pandas as pd
from io import BytesIO

from excel_reader import read_supplier_data, SupplierType


app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/uploadFile/")
async def create_upload_file(file: UploadFile):
    if file.filename.endswith('.xlsx'):
        # Read it, 'f' type is bytes
        f = await file.read()
        excelfile = BytesIO(f)
        wb = read_supplier_data(supplier_type=SupplierType.ANQUANQIAN_1, 
                                       file = excelfile)

        print(wb)
        return True

    else:
        raise HTTPException(status_code=404, detail="Item not found")