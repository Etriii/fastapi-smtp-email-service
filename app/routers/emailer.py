from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, EmailStr
from app.utils.emailer import send_email

router = APIRouter()

class EmailRequest(BaseModel):
    to: EmailStr
    subject: str
    body: str

@router.post("/send-email")
def email_endpoint(data: EmailRequest):
    result = send_email(data.to, data.subject, data.body)
    if "successfully" in result:
        return {"message": result}
    raise HTTPException(status_code=500, detail=result)
