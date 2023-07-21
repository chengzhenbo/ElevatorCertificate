import uvicorn
from fastapi import FastAPI
from pathlib import Path
from mail.mail import (MessageSchema, 
                       send_email_plain,
                       send_email_attachedfile)

HERE = Path(__file__).resolve().parent

app = FastAPI(title='How to Send Email')
 
@app.get('/')
def index():
    return 'Hello World'


@app.get('/send-email-plain/asynchronous')
async def send_email_plain_asynchronous():
    subject="过期提醒"
    message="你好，型式试验报告过期，请及时替换。"
    await send_email_plain(message=MessageSchema(subject=subject,message=message),
                           recipients=['czb@zjut.edu.cn','zhbcheng@gmail.com'])
    return 'Success'

@app.get('/send-email-attachedfile/asynchronous')
async def send_email_attachedfile_asynchronous():
    subject="过期提醒"
    message="你好，附件的型式试验报告临近过期，请及时替换文件。"

    file_name = HERE / 'attachedfiles'/'td.pdf'
    await send_email_attachedfile(message=MessageSchema(subject=subject,message=message),
                           recipients=['czb@zjut.edu.cn','zhbcheng@gmail.com'], 
                           filename=file_name)
    return 'Success'


if __name__ == '__main__':
    uvicorn.run('main:app', reload=True)