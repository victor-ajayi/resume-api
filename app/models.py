from sqlalchemy import ARRAY, Column, Integer, String
from sqlalchemy.sql.expression import func
from sqlalchemy.sql.sqltypes import TIMESTAMP

from app.database import Base


class Profile(Base):
    __tablename__ = "profile"

    first_name = Column(String, primary_key=True, nullable=False)
    last_name = Column(String, nullable=False)
    bio = Column(String)
    email = Column(String, nullable=False)
    github = Column(String, nullable=False)


class Stack(Base):
    __tablename__ = "stack"

    name = Column(String, primary_key=True, nullable=False)
    created_at = Column(
        TIMESTAMP(timezone=True),
        nullable=False,
        server_default=func.now(),
    )
    updated_at = Column(TIMESTAMP(timezone=True), onupdate=func.now())


class Projects(Base):
    __tablename__ = "projects"

    title = Column(String, primary_key=True)
    description = Column(String, nullable=False)
    year = Column(Integer, nullable=False)
    stack = Column(ARRAY(String), nullable=False)
    tasks = Column(ARRAY(String), nullable=False)


class Languages(Base):
    __tablename__ = "languages"

    name = Column(String, primary_key=True)


class Education(Base):
    __tablename__ = "education"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    degree = Column(String, nullable=False)
    level = Column(String, nullable=False)
    start_year = Column(Integer)
    end_year = Column(Integer, nullable=False)
