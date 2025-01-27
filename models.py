from pydantic import BaseModel, EmailStr, Field
from typing import List, Dict

class EmailSchema(BaseModel):
    email: List[EmailStr]  # List of valid email addresses
    subject: str  # Email subject
    body: Dict[str, str]  # Dictionary with "title" and "message" for the email body
    
    class Config:
        schema_extra = {
            "example": {
                "email": ["shahramsamar2010@gmail.com"],
                "subject": "FastApi",
                "body": {
                    "title": "FastApi",
                    "message": "This email is sent by FastApi"
                }
            }
        }
