import datetime
from typing import Optional
from sqlmodel import Field, SQLModel, Enum, Relationship
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
import uuid

class StatusEnum(str, Enum):
    pending = "pending"
    processing = "processing"
    completed = "completed"
    failed = "failed"

class Users(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    first_name: str
    last_name: str
    api_key: Optional[str] = Field(default=str(uuid.uuid4()), index=True)
    email: str
    restricted: Optional[bool] = Field(default=False)
    deactivated: Optional[datetime.datetime] = Field(default=None)
    created: datetime.datetime = Field(default_factory=datetime.datetime.utcnow, nullable=False)
    updated: datetime.datetime = Field(default_factory=datetime.datetime.utcnow, nullable=False)
  

class Transcripts(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    user_id: Optional[int] = Relationship(
        sa_relationship=relationship("user_transcripts", cascade="all, delete", back_populates="transcripts")
    )
    content: Optional[str] = Field(default=None)
    created: datetime.datetime = Field(default_factory=datetime.datetime.utcnow, nullable=False)
    updated: datetime.datetime = Field(default_factory=datetime.datetime.utcnow, nullable=False)
  
    
class Uploads(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    user_id: Optional[int] = Relationship(
        sa_relationship=relationship("user_uploads", cascade="all, delete", back_populates="uploads")
    )
    transcript_id: Optional[int] = Field(default=None, index=True, foreign_key="transcripts.id")
    filename: str
    file_id: str = Field(index=True)
    created: datetime.datetime = Field(default_factory=datetime.datetime.utcnow, nullable=False)
    updated: datetime.datetime = Field(default_factory=datetime.datetime.utcnow, nullable=False)

class Queue(SQLModel, table=True):
    class Config:
        arbitrary_types_allowed = True
        
    id: Optional[int] = Field(default=None, primary_key=True)
    user_id: Optional[int] = Field(default=None, index=True, foreign_key="users.id")
    transcript_id: Optional[int] = Field(default=None, index=True, foreign_key="transcripts.id")
    status: StatusEnum = Field(default=StatusEnum.pending, index=True)
    created: datetime.datetime = Field(default_factory=datetime.datetime.utcnow, nullable=False)
    updated: datetime.datetime = Field(default_factory=datetime.datetime.utcnow, nullable=False)
