from pydantic import BaseModel
from typing import Optional
from typing import Any

class ApiResponseModel(BaseModel):
  status: bool
  message: str
  error_code: Optional[str] = None
  data: Any

    
