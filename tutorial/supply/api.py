from fastapi import FastAPI,UploadFile,HTTPException
from io import BytesIO

from starlette import status
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from model.models import Book as ModelBook
from model.schema import Book as SchemaBook


from excel_reader import read_supplier_data, SupplierType


app = FastAPI()

session_maker = sessionmaker(bind=create_engine("sqlite:///models.db"))

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get('/book/')
async def book():
    with session_maker() as session:
        book = session.query(ModelBook).all()
    return book

@app.post('/book/', response_model=SchemaBook)
def book(book: SchemaBook):
    with session_maker() as session:
        db_book = ModelBook(title=book.title, rating=book.rating)
        session.add(db_book)
        session.commit()
    return db_book

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