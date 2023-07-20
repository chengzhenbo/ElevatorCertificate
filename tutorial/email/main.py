# main.py
from fastapi import FastAPI
from fastapi.exceptions import HTTPException
from pydantic import BaseModel
from smtplib import SMTP_SSL
from email.mime.text import MIMEText

app = FastAPI()

OWN_EMAIL = "1510677989@qq.com"
OWN_EMAIL_PASSWORD = "ivumeyhfaghbigdj"

class EmailBody(BaseModel):
    to: str
    subject: str
    message: str

@app.post("/email")
async def send_email(body: EmailBody):
    try:
        msg = MIMEText(body.message, "html")
        msg['Subject'] = body.subject
        msg['From'] = f'Denolyrics <{OWN_EMAIL}>'
        msg['To'] = body.to

        port = 465  # For SSL

        # Connect to the email server
        server = SMTP_SSL("smtp.qq.com", port)
        server.login(OWN_EMAIL, OWN_EMAIL_PASSWORD)
        # Send the email
        server.send_message(msg)
        server.quit()
        return {"message": "Email sent successfully"}

    except Exception as e:
        raise HTTPException(status_code=500, detail=e)