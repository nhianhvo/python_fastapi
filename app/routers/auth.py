from datetime import timedelta
from fastapi import APIRouter, HTTPException, Depends
from fastapi.security import OAuth2PasswordBearer
from app.models.authenticate_model import LoginRequest, LoginResponse, RegisterRequest, RegisterResponse
from app.models.response_model import ResponseModel
from app.services.auth_service import ACCESS_TOKEN_EXPIRE_MINUTES, verify_password, get_password_hash, create_access_token

router = APIRouter()

# Giả sử có một user trong database
fake_user_db = [
    {
        "username": "anhvn",
        "password": get_password_hash("123456")
    }
]

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

@router.post("/token", response_model=ResponseModel[LoginResponse])
async def login_access_token(form_data: LoginRequest):
    try:
        print(form_data.password)
    
        user = next((user for user in fake_user_db if user["username"] == form_data.username), None)
        print(user["password"])
        if not user or not verify_password(form_data.password, user["password"]):
            raise HTTPException(status_code=400, detail="Incorrect username or password")
        
        access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
        access_token = create_access_token(
            data={"sub": user["username"]}, expires_delta=access_token_expires
        )
        return ResponseModel(
            code=200,
            status="success",
            data=LoginResponse(access_token=access_token, token_type="bearer"),
            message="Login successfully"
        )
   
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    
     
