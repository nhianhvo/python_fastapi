from fastapi import FastAPI, HTTPException , Request
from typing import Dict, List

from app.routers import student, auth


app = FastAPI(title="Student Management API")

app.include_router(student.router, prefix="/api", tags=["students"])
app.include_router(auth.router, prefix="/api", tags=["auth"])