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
    user_id: Optional[int] = Field(
        default=None, index=True, foreign_key="users.id")
    filename: str
    file_id: Optional[str]
    status: StatusEnum = Field(default="pending")
    created: datetime.datetime = Field(default=datetime.datetime.utcnow)
    updated: datetime.datetime = Field(default=datetime.datetime.utcnow)
