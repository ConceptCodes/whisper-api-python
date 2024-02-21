from fastapi import APIRouter
from core.models.response import ApiReponseModel

from core.util.response import send_success_response

router = APIRouter()

@router.get("/healthcheck", 
            tags=["healthcheck"], 
            summary="Health check for the service.", 
            description="Health check for the service.",
            )
async def alive() -> ApiReponseModel:
  return send_success_response("Service is alive")
