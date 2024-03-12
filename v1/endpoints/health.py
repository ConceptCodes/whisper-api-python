from fastapi import APIRouter
from core.models.response import ApiResponseModel, HealthCheckResponse
from core.util.response import send_success_response
from lib.db import db

router = APIRouter()


@router.get("/healthcheck",
            tags=["healthcheck"],
            summary="Health check for the service.",
            description="Health check for the service.",
            )
async def alive() -> ApiResponseModel:
    data = list()
    data.append(HealthCheckResponse(
        service="database", status=db.health_check()))
    return send_success_response("Service is alive", data)
