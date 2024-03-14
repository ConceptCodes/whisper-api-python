from fastapi import APIRouter
from core.schemas.response import ApiResponseModel, HealthCheckResponse
from core.util.response import send_success_response
from lib.db import db_client

router = APIRouter()


@router.get("/healthcheck",
            tags=["healthcheck"],
            summary="Health check for the service.",
            description="Health check for the service.",
            )
async def alive() -> ApiResponseModel:
    data = list()
    data.append(HealthCheckResponse(
        service="database", status=db_client.health_check()))
    return send_success_response("Service is alive", data)
