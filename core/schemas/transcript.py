import datetime
from pydantic import BaseModel


class GetStatusResponse(BaseModel):
    status: str
    updated_at: datetime.datetime


class TranscriptCreateRequest(BaseModel):
    file_path: str