from pathlib import Path
from fastapi import FastAPI, Request,BackgroundTasks
from fastapi.responses import JSONResponse
from fastapi_mail import FastMail, MessageSchema, ConnectionConfig
from models import EmailSchema  # Assuming `EmailSchema` is defined in `models`
from pydantic_settings import BaseSettings

import os

# Get the directory of the current script (main.py)
current_dir = os.path.dirname(os.path.abspath(__file__))

# Define the relative path to the email templates folder
relative_path = "template/"

# Combine the current directory with the relative path to create an absolute path
template_folder_path = os.path.abspath(os.path.join(current_dir, relative_path))

# print(f"Template folder absolute path: {template_folder_path}")


# Configuration class for email settings
class EmailSettings(BaseSettings):
    MAIL_USERNAME: str = 'shahramsamar2010@gmail.com'
    MAIL_PASSWORD: str = 'hcnn tyxv eyya hjuy'  # App-specific password for Gmail
    MAIL_FROM: str = 'shahramsamar2010@gmail.com'
    MAIL_PORT: int = 587
    MAIL_SERVER: str = 'smtp.gmail.com'
    MAIL_STARTTLS: bool = True
    MAIL_SSL_TLS: bool = False
    USE_CREDENTIALS: bool = True
    TEMPLATE_FOLDER: str = template_folder_path  # Absolute path

# Load email settings
email_settings = EmailSettings()

# FastAPI app instance
app = FastAPI(
    title="FastApi Send email by BackgroundTasks",
    description="send email by BackgroundTasks",
    version="0.0.1",
    terms_of_service="https://example.com/terms",
    contact={
        "name": "Shahram Samar",
        "url": "https://shahramsamar.github.io/",
        "email": "shahramsamar2010@gmail.com",
    },
    license_info={
        "name": "MIT",
        "url": "https://opensource.org/licenses/MIT",
    },
  
)




# Endpoint to send emails
@app.post('/email', tags=["Send Email using Background Tasks"])
async def send_email(data: EmailSchema, background_tasks: BackgroundTasks):
    # Message configuration
    message = MessageSchema(
        subject=data.subject,
        recipients=data.dict().get('email'),  # List of recipients
        template_body=data.dict().get("body"),  # Template context
        subtype='html',  # Email format
    )
    
    # Initialize FastMail with email settings
    fm = FastMail(
        ConnectionConfig(
            MAIL_USERNAME=email_settings.MAIL_USERNAME,
            MAIL_PASSWORD=email_settings.MAIL_PASSWORD,
            MAIL_FROM=email_settings.MAIL_FROM,
            MAIL_PORT=email_settings.MAIL_PORT,
            MAIL_SERVER=email_settings.MAIL_SERVER,
            MAIL_STARTTLS=email_settings.MAIL_STARTTLS,
            MAIL_SSL_TLS=email_settings.MAIL_SSL_TLS,
            USE_CREDENTIALS=email_settings.USE_CREDENTIALS,
            TEMPLATE_FOLDER=email_settings.TEMPLATE_FOLDER,
        )
    )
    
    # Send email using the specified template
    background_tasks.add_task(fm.send_message,message, template_name='email.html')
    return JSONResponse(status_code=200, content={"message": "Email has been sent"})
