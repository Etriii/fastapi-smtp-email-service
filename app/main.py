from fastapi import FastAPI
from app.routers import emailer

app = FastAPI()

app.include_router(emailer.router, prefix="/api/email")
