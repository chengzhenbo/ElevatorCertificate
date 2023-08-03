from fastapi import FastAPI,UploadFile,HTTPException
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
        product_parts = read_supplier_data(supplier_type=SupplierType.ANQUANQIAN_1, 
                                       file = excelfile)

        if product_parts is not None:
            print(product_parts)
            return True
        else:
            raise HTTPException(status_code=404, detail="Data reader is wrong")

    else:
        raise HTTPException(status_code=404, detail="File can not open")