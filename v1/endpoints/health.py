from fastapi import APIRouter

from core.util.response import send_success_response

router = APIRouter()

@router.get("/healthcheck", 
            tags=["healthcheck"], 
            summary="Health check for the service.", 
            description="Health check for the service.")
def alive():
    return send_success_response("Service is alive")
