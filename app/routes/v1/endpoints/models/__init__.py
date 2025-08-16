import uuid
from typing import Literal
from fastapi import APIRouter
from pydantic import BaseModel, RootModel

import app.errors.error as http_error

router = APIRouter()


class Model(BaseModel):
    id: str
    framework: Literal["PyTorch"]
    type: Literal["Classification", "Object Detection"]
    name: str
    description: str


class ModelList(RootModel):
    root: list[Model]


CV_MODEL_LIST = ModelList.model_validate(
    [
        Model(
            id=str(uuid.uuid4()),
            name="YOLO (Ultralytics)",
            description="Object detection and instance segmentation",
            type="Object Detection",
            framework="PyTorch",
        ),
        Model(
            id=str(uuid.uuid4()),
            name="Resnet18",
            description="Image classification",
            type="Classification",
            framework="PyTorch",
        ),
    ]
)


@router.get("")
async def fetch() -> ModelList:
    return CV_MODEL_LIST


@router.get("/{id}")
async def fetch_by_id(id: str) -> Model:
    """Return a single model by ID"""
    for model in CV_MODEL_LIST.root:
        if model.id == id:
            return model
    raise http_error.ModelNotFound()