import datetime
from typing import Optional
from sqlmodel import Field, SQLModel, Enum

class StatusEnum(str, Enum):
    pending = "pending"
    processing = "processing"
    completed = "completed"
    failed = "failed"

class Uploads(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    userId: Optional[int] = Field(
        default=None, index=True, foreign_key="users.id")
    transcriptId: Optional[int] = Field(
        default=None, index=True, foreign_key="transcripts.id")
    filename: str
    fileId: str
    status: StatusEnum = Field(default="pending")
    created: datetime.datetime = Field(default=datetime.datetime.utcnow)
    updated: datetime.datetime = Field(default=datetime.datetime.utcnow)
