from pydantic import BaseModel
from typing import Optional
from typing import Any

class OnboardUserRequestDto(BaseModel):
  first_name: str
  last_name: str
  email: str

class OnboardUserResponseDto(OnboardUserRequestDto):
  api_key: str