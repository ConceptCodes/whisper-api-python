
from pydantic import BaseModel

class ApiReponseModel(BaseModel):
    status: str
    message: str
    data: dict

    
