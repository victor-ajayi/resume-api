from fastapi import APIRouter, Depends
from pydantic import TypeAdapter
from sqlalchemy.orm import Session

from app import models
from app.database import get_db
from app.schemas import Education, Languages, Profile, Projects, Stack

router = APIRouter(tags=["Profile"])


@router.get("/", status_code=200)
def get_profile(db: Session = Depends(get_db)):
    profile = TypeAdapter(Profile).dump_python(
        db.query(models.Profile).first(), mode="json"
    )
    stack = [
        s["name"]
        for s in TypeAdapter(list[Stack]).dump_python(
            db.query(models.Stack).all(), mode="json"
        )
    ]
    projects = TypeAdapter(list[Projects]).dump_python(
        db.query(models.Projects).all(), mode="json"
    )
    languages = [
        lang["name"]
        for lang in TypeAdapter(list[Languages]).dump_python(
            db.query(models.Languages).all(), mode="json"
        )
    ]
    education = TypeAdapter(Education).dump_python(
        db.query(models.Education).first(), mode="json"
    )

    response = {
        "profile": profile,
        "stack": stack,
        "projects": projects,
        "languages": languages,
        "education": education,
    }

    return response
