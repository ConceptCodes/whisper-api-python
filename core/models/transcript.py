import datetime
from typing import Optional
from sqlmodel import Field, SQLModel

class Transcripts(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    userId: Optional[int] = Field(
        default=None, index=True, foreign_key="users.id")
    content: Optional[str] = Field(default=None)
    created: datetime.datetime = Field(default=datetime.datetime.utcnow)
    updated: datetime.datetime = Field(default=datetime.datetime.utcnow)
