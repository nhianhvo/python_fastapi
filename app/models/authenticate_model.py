from pydantic import BaseModel

class LoginRequest(BaseModel):
    username: str
    password: str

class LoginResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"
    
class RegisterRequest(BaseModel):
    username: str
    password: str
    email: str
    full_name: str

class RegisterResponse(BaseModel):
    id: int
    username: str
    email: str
    full_name: str
