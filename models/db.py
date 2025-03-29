from models.base import Base
from sqlalchemy import Column, null
from sqlalchemy.types import Integer, String, DateTime
import datetime
from sqlalchemy.orm import relationship


class Profile(Base):
    __tablename__ = "profile"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)
    gender = Column(String)
    description = Column(String)
    interests = Column(String)
    contact = Column(String)
    created_ts = Column(DateTime, nullable=False)
    updated_ts = Column(DateTime, nullable=False)
    
    comment = relationship(argument="Comment",
                                            back_populates="profile")

class Comment(Base):
    __tablename__ = "comment"
    id = Column(Integer, primary_key=True)
    author_name = Column(String, nullable=False)
    content = Column(String, nullable=False)
    created_ts = Column(DateTime, nullable=False)
    updated_ts = Column(DateTime, nullable=False)
