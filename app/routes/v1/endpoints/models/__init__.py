from typing import Literal
from fastapi import APIRouter, Query

import app.errors.error as http_error
from app.schemas import Model, SettingConfig
from app.constants import CV_MODEL_LIST, MODELS_SETTINGS



router = APIRouter()


@router.get("/settings")
async def get_settings(type: Literal["Classification", "Object Detection"] = Query(...)) -> list[SettingConfig]:
    return MODELS_SETTINGS.root[type]
    

@router.get("")
async def fetch() -> list[Model]:
    return CV_MODEL_LIST


@router.get("/{id}")
async def fetch_by_id(id: str) -> Model:
    """Return a single model by ID"""
    for model in CV_MODEL_LIST:
        if model.id == id:
            return model
    raise http_error.ModelNotFound()