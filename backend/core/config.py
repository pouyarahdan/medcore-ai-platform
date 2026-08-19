import os


class Settings:
    PROJECT_NAME = os.getenv(
        "MEDCORE_PROJECT_NAME",
        "MedCore AI Platform"
    )

    VERSION = os.getenv(
        "MEDCORE_VERSION",
        "1.0.0"
    )

    DEBUG = os.getenv(
        "MEDCORE_DEBUG",
        "True"
    ).lower() == "true"


settings = Settings()