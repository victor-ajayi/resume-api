from pydantic import BaseModel


class Profile(BaseModel):
    first_name: str
    last_name: str
    bio: str
    email: str
    github: str


class Stack(BaseModel):
    name: str


class Projects(BaseModel):
    title: str
    description: str
    year: int
    stack: list[str]
    tasks: list[str]


class Languages(BaseModel):
    name: str


class Education(BaseModel):
    name: str
    degree: str
    level: str
    start_year: int
    end_year: int
