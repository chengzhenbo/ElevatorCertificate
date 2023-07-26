from fastapi import FastAPI
import uvicorn

from estamp import Stamp

app = FastAPI()

@app.get("/")
def root():
    stamp = Stamp(pdf_inputname='C8950.pdf', stamp_page='L')
    outfile = stamp.run()
    return{'outputfile':outfile}

if __name__ == '__main__':
    uvicorn.run('main:app', reload=True)
