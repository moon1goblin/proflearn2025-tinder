from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from starlette.types import HTTPExceptionHandler
from models.base import get_db
from models.db import Profile
import datetime
from pydantic import BaseModel

profile = APIRouter(prefix="/profile", tags=["Profile"])


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


class ProfilePost(BaseModel):
    # id: int
    name: str
    age: int
    gender: str
    description: str
    interests: str
    contact: str
    # created_ts: datetime.datetime
    # updated_ts: datetime.datetime


@profile.get("")
def get_profiles(
    gender: str | None,
    limit: int,
    offset: int,
    page: int | None = None,
    min_age: int | None = None,
    max_age: int | None = None,
    db: Session = Depends(get_db),
):
    if gender not in ["мужской", "женский"]:
        raise HTTPException(status_code=400, detail="Неверный формат пола")
    query = db.query(Profile)
    if min_age is not None:
        query = query.filter(Profile.age > min_age)
    if max_age is not None:
        query = query.filter(Profile.age < max_age)
    if limit is None:
        limit = 0
    profiles: list[Profile] = query.all()
    profiles = profiles[offset : limit + offset]

    result = []
    for item in profiles:
        result.append(ProfileGet.model_validate(item, from_attributes=True))

    return result


@profile.get("/{id}")
def get_profile(profile_id: int, db: Session = Depends(get_db)):
    profile = db.query(Profile).filter(Profile.id == profile_id).one_or_none()
    if profile is None:
        raise HTTPException(status_code=404, detail="Профиль не найден")
    return ProfileGet.model_validate(profile, from_attributes=True)


@profile.post("")
def create_profile(data: ProfilePost, db: Session = Depends(get_db)):
    new_profile = Profile(
        name=data.name,
        age=data.age,
        gender=data.gender,
        description=data.description,
        interests=data.interests,
        contact=data.contact,
    )
    db.add(new_profile)
    db.commit()
