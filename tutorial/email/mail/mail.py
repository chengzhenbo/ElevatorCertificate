
from smtplib import SMTP_SSL
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from typing import List
from pydantic import EmailStr, BaseModel
from os.path import basename

from mail.config import settings


class EmailSchema(BaseModel):
    email: List[EmailStr]

class MessageSchema(BaseModel):
    subject: str
    message: str


async def send_email_plain(message: MessageSchema, 
                           recipients:EmailSchema)-> None:
    msg = MIMEMultipart()
    msg['Subject'] = message.subject
    msg['From'] = f'{settings.MAIL_FROM_NAME}<{settings.MAIL_FROM}>'
    msg['To'] = ", ".join(recipients)
    body = MIMEText(message.message, 'plain')
    msg.attach(body)

    # Connect to the email server
    server = SMTP_SSL(settings.MAIL_SERVER, settings.MAIL_PORT)
    server.login(settings.MAIL_FROM, settings.MAIL_PASSWORD)
    # Send the email
    server.send_message(msg)
    server.quit()

async def send_email_attachedfile(message: MessageSchema, 
                           recipients:EmailSchema,
                           filename:str)-> None:
    msg = MIMEMultipart()
    msg['Subject'] = message.subject
    msg['From'] = f'{settings.MAIL_FROM_NAME}<{settings.MAIL_FROM}>'
    msg['To'] = ", ".join(recipients)
    body = MIMEText(message.message, 'plain')
    msg.attach(body)

    with open(filename, 'rb') as f:
        part = MIMEApplication(f.read(), Name=basename(filename))
        part['Content-Disposition'] = 'attachment; filename="{}"'.format(basename(filename))
        msg.attach(part)

    # Connect to the email server
    server = SMTP_SSL(settings.MAIL_SERVER, settings.MAIL_PORT)
    server.login(settings.MAIL_FROM, settings.MAIL_PASSWORD)
    # Send the email
    server.send_message(msg)
    server.quit()
