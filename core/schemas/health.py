from pydantic import BaseModel


class HealthCheckResponse(BaseModel):
    service: str
    status: bool
