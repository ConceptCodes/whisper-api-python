from fastapi import APIRouter
from sqlmodel import Session

from core.models.db import Users
from core.models.dto import OnboardUserRequestDto, OnboardUserResponseDto
from core.models.response import ApiResponseModel
from core.util.response import send_error_response, send_success_response

from lib.db import db

router = APIRouter(prefix="/auth")

@router.post("/onboard", 
            tags=["auth"], 
            summary="Onboard a user to the service")
async def onboard_user(user: OnboardUserRequestDto) -> ApiResponseModel:
  try:
    engine = db.get_engine()
    tmp = Users(first_name=user.first_name, email=user.email, last_name=user.last_name)
    with Session(engine) as session:
      session.add(tmp)
      session.commit()
      session.refresh(tmp)
    data = OnboardUserResponseDto(api_key=tmp.api_key, first_name=tmp.first_name, last_name=tmp.last_name, email=tmp.email)
    return send_success_response("User has onboarded successfully", data)  
  except Exception as e:
    return send_error_response(str(e))