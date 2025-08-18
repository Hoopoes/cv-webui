import uuid
from app.schemas.models_schema import Model


CV_MODEL_LIST = [
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
