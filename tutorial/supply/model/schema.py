# build a schema using pydantic
from pydantic import BaseModel

class Book(BaseModel):
    title: str
    rating: int

    

class Author(BaseModel):
    name:str
    age:int

    


        