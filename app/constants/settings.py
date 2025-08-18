from app.schemas.models_schema import SettingConfig, SettingList



MODELS_SETTINGS = SettingList(
    root={
        "Classification": [
            SettingConfig(
                name="conf",
                label="Confidence Threshold",
                type="slider",
                min=0.0,
                max=1.0,
                step=0.01,
                default=0.5,
            ),
        ],
        "Object Detection": [
            SettingConfig(
                name="iou",
                label="IoU Threshold",
                type="slider",
                min=0.0,
                max=1.0,
                step=0.01,
                default=0.5,
            ),
            SettingConfig(
                name="conf",
                label="Confidence Threshold",
                type="slider",
                min=0.0,
                max=1.0,
                step=0.01,
                default=0.5,
            ),
            SettingConfig(
                name="padding",
                label="Padding",
                type="number",
                min=0.0,
                max=100.0,
                step=0.1,
                default=10.0,
            ),
        ],
    }
)