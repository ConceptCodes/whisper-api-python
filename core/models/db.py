import datetime
from typing import Optional
from sqlmodel import Field, SQLModel, Enum

class StatusEnum(str, Enum):
    pending = "pending"
    processing = "processing"
    completed = "completed"
    failed = "failed"

class Users(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    displayName: str
    apiKey: Optional[str] = Field(default=None, index=True)
    email: str
    restricted: Optional[bool] = Field(default=False)
    deactivated: Optional[datetime.datetime] = Field(default=None)
    created: datetime.datetime = Field(default=datetime.datetime.utcnow)
    updated: datetime.datetime = Field(default=datetime.datetime.utcnow)

class Transcripts(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    userId: Optional[int] = Field(default=None, index=True, foreign_key="users.id")
    content: Optional[str] = Field(default=None)
    created: datetime.datetime = Field(default=datetime.datetime.utcnow)
    updated: datetime.datetime = Field(default=datetime.datetime.utcnow)

class Uploads(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    userId: Optional[int] = Field(default=None, index=True, foreign_key="users.id")
    transcriptId: Optional[int] = Field(default=None, index=True, foreign_key="transcripts.id")
    filename: str
    fileId: str
    created: datetime.datetime = Field(default=datetime.datetime.utcnow)
    updated: datetime.datetime = Field(default=datetime.datetime.utcnow)

class Queue(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    userId: Optional[int] = Field(default=None, index=True, foreign_key="users.id")
    transcriptId: Optional[int] = Field(default=None, index=True, foreign_key="transcripts.id")
    status: StatusEnum = Field(default="pending", index=True)
    created: datetime.datetime = Field(default=datetime.datetime.utcnow)
    updated: datetime.datetime = Field(default=datetime.datetime.utcnow)