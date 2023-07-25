from pathlib import Path
from config import settings
from fastapi import FastAPI

HERE = Path(__file__).resolve().parent
app = FastAPI()

@app.get("/")
def root():
    return{'message':'Hello.'}

if __name__ == '__main__':
    print(HERE)
    print(settings.ESTAMP_PATH)
