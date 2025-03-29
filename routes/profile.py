import datetime

from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from models.base import get_db
from models.db import Profile
from pydantic import BaseModel
profile = APIRouter(prefix="/api/profiles", tags=["Profile"])

class ProfileGet(BaseModel):
    id: int
    name: str
    age: int
    gender: str
    description: str
    interests: str
    contact: str
    created_ts: datetime.datetime
    updated_ts: datetime.datetime

@profile.get("")
def get_profiles(
    gender: str | None = None,
    offset: int | None = None,
    limit: int | None = None,
    min_age: int | None = None,
    max_age: int | None = None,
    db: Session = Depends(get_db)
):
    if gender is not None and gender not in ["мужской", "женский"]:
        raise HTTPException(status_code=400, detail="Неверный формат пола")
    query = db.query(Profile)
    if min_age is not None:
        query = query.filter(Profile.age > min_age)
    if max_age is not None:
        query = query.filter(Profile.age < max_age)
    if offset is None:
        offset = 0
    if limit is None:
        limit = 10
    profiles: list[Profile] = query.all()
    profiles = profiles[offset:limit+offset]

    result = []
    for item in profiles:
        result.append(ProfileGet.model_validate(item))

    return result
