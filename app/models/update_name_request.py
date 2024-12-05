from pydantic import BaseModel

class UpdateNameRequest(BaseModel):
    name: str