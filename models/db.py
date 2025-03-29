# from models.base import Base
# from sqlalchemy import Column, ForeignKey, null
# from sqlalchemy.types import Integer, String, DateTime
# import datetime
# from sqlalchemy.orm import relationship
#
#
# class Profile(Base):
#     __tablename__ = "profile"
#     id = Column(Integer, primary_key=True)
#     name = Column(String)
#     age = Column(Integer)
#     gender = Column(String)
#     description = Column(String)
#     interests = Column(String)
#     contact = Column(String)
#     created_ts = Column(DateTime, nullable=False)
#     updated_ts = Column(DateTime, nullable=False)
#
#     comment = relationship(argument="Comment",
#                                             back_populates="profile")
#
# class Comment(Base):
#     __tablename__ = "comment"
#     id = Column(Integer, primary_key=True)
#     author_name = Column(String, nullable=False)
#     content = Column(String, nullable=False)
#     created_ts = Column(DateTime, nullable=False)
#     updated_ts = Column(DateTime, nullable=False)
#     # TODO: try rename this shit to profile_id
#     profile_ed = Column("Profile", ForeignKey("profile.id"))
#
#     profile = relationshipfrom models.base import Base

from models.base import Base
from sqlalchemy import Column, ForeignKey
from sqlalchemy.types import Integer, String, DateTime
from sqlalchemy.orm import relationship
import datetime

class Profile(Base):
    __tablename__ = "profile"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    age = Column(Integer)
    gender = Column(String, nullable=False)
    description = Column(String)
    interests = Column(String)
    contact = Column(String, nullable=False)
    created_ts = Column(DateTime, nullable=False, default=datetime.datetime.now)
    updated_ts = Column(DateTime, nullable=False, default=datetime.datetime.now)

    comments = relationship("Comment", back_populates="profile")

class Comment(Base):
    __tablename__ = "comment"
    id = Column(Integer, primary_key=True)
    author_name = Column(String, nullable=False)
    content = Column(String, nullable=False)
    created_ts = Column(DateTime, nullable=False, default=datetime.datetime.now)
    updated_ts = Column(DateTime, nullable=False, default=datetime.datetime.now)
    profile_id = Column(Integer, ForeignKey("profile.id"))

    profile = relationship("Profile", back_populates="comments")("Profile", back_populates="comments")
