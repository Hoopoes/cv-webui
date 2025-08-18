from typing import Literal
from fastapi import APIRouter
from pydantic import BaseModel, ConfigDict, Field, RootModel

router = APIRouter()

ModelType = Literal["Classification", "Object Detection"]

class Model(BaseModel):
    id: str
    framework: Literal["PyTorch"]
    type: ModelType
    name: str
    short_description: str = Field(alias="shortDescription")
    description: str
    
    model_config = ConfigDict(populate_by_name=True)


class SettingConfig(BaseModel):
    name: str = Field(..., description="Internal name of the setting")
    label: str = Field(..., description="User-facing label")
    type: Literal["slider", "number"] = Field(..., description="UI control type")
    min: float
    max: float
    step: float
    default: float


class SettingList(RootModel):
    root: dict[ModelType, list[SettingConfig]]