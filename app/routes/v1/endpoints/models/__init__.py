import uuid
from typing import Literal
from fastapi import APIRouter
from pydantic import BaseModel, ConfigDict, Field, RootModel

import app.errors.error as http_error

router = APIRouter()


class Model(BaseModel):
    id: str
    framework: Literal["PyTorch"]
    type: Literal["Classification", "Object Detection"]
    name: str
    short_description: str = Field(alias="shortDescription")
    description: str
    
    model_config = ConfigDict(populate_by_name=True)


class ModelList(RootModel):
    root: list[Model]


CV_MODEL_LIST = ModelList.model_validate(
    [
        Model(
            id=str(uuid.uuid4()),
            name="YOLO (Ultralytics)",
            short_description="Object detection and instance segmentation",
            description="Object detection and instance segmentation",
            type="Object Detection",
            framework="PyTorch",
        ),
        Model(
            id=str(uuid.uuid4()),
            name="Resnet18",
            short_description="Image classification",
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