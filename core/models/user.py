import datetime
from typing import Optional
from sqlmodel import Field, SQLModel


class Users(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    displayName: str
    apiKey: Optional[str] = Field(default=None, index=True)
    email: str
    restricted: Optional[bool] = Field(default=False)
    deactivated: Optional[datetime.datetime] = Field(default=None)
    created: datetime.datetime = Field(default=datetime.datetime.utcnow)
    updated: datetime.datetime = Field(default=datetime.datetime.utcnow)
